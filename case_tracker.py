from datetime import date, datetime
import pandas as pd
import numpy as np
from math import pi
from bokeh.plotting import figure, show, ColumnDataSource, curdoc
from bokeh.models import DaysTicker, HoverTool, CustomJS, Select, DatePicker, Div
from bokeh.models.annotations import Title
from bokeh.layouts import column, row
from bokeh.palettes import Category20c
from bokeh.transform import cumsum
#from bokeh.models.widgets import Button

data = pd.read_csv('cdph-state-totals.csv')#('latimes-state-totals.csv')
data['date_time'] = pd.to_datetime(data['date'])
data = data.sort_values(by=['date_time'], ascending=True)
data['new_confirmed_cases'] = data['confirmed_cases'].diff().fillna(data['confirmed_cases'])
data['new_deaths'] = data['deaths'].diff().fillna(0)
start = data['date_time'].min()
end = data['date_time'].max()
selected = "Cases"
selectedDate = "2020-07-15"

dataRace = pd.read_csv('cdph-race-ethnicity.csv')
dataRace['date_time'] = pd.to_datetime(dataRace['date'])
dataRace = dataRace.loc[dataRace['age'] == 'all']
dataRace = dataRace.sort_values(by=['date_time', 'race'], ascending=True)
dataRace = dataRace[['date_time', 'race', 'confirmed_cases_percent', 'deaths_percent', 'confirmed_cases_total', 'deaths_total']]
numRace = len(dataRace['race'].unique())

dataRaceTotal = dataRace.groupby(['date_time']).agg({'confirmed_cases_percent': 'sum', 'deaths_percent': 'sum'}).rename(columns={'confirmed_cases_percent':'total_cases_percent', 'deaths_percent': 'total_deaths_percent'})
dataRace = pd.merge(dataRace, dataRaceTotal, on='date_time')

def getDataRaceSelected(selectedDate, selected):
    if dataRace.loc[dataRace['date_time'] == selectedDate].empty:
        dRaceSelected = pd.DataFrame({'date_time' : [], 'race' : [], 'angle' : [], 'percentage' : [], 'color' : [], 'total' : []})        
    else:
        dRaceSelected = dataRace.loc[dataRace['date_time'] == selectedDate].copy()
        dRaceSelected.reset_index()#.rename(columns={'index':'raceIdx'})
        if selected == 'Cases':
            dRaceSelected['angle'] = dRaceSelected['confirmed_cases_percent']/dRaceSelected['total_cases_percent'] * 2*pi
            dRaceSelected['percentage'] = dRaceSelected['confirmed_cases_percent']
            dRaceSelected['total'] = dRaceSelected['confirmed_cases_total']
        elif selected == 'Deaths':
            dRaceSelected['angle'] = dRaceSelected['deaths_percent']/dRaceSelected['total_deaths_percent'] * 2*pi
            dRaceSelected['percentage'] = dRaceSelected['deaths_percent']
            dRaceSelected['total'] = dRaceSelected['deaths_total']
        dRaceSelected['color'] = Category20c[6]
    #print(dRaceSelected.head())
    return dRaceSelected
        


div = Div(text="""<b>California State Covid-19 Case Tracker</b><br>
Data Source by California Department of Public Health daily release also accessible at <a href="https://github.com/datadesk/california-coronavirus-data">Github repository</a> with file names as cdph-state-totals.csv and cdph-race-etnicity.csv<br> 
<ul>
<li>Accumulative Cases and Deaths data (cdph-state-totals.csv) was originated from <a href="https://www.cdph.ca.gov/Programs/OPA/Pages/New-Release-2020.aspx">https://www.cdph.ca.gov/Programs/OPA/Pages/New-Release-2020.aspx</a></li>
<li>Race and etnicity data (cdph-race-etnicity.csv) was originated from <a href="https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/COVID-19/Race-Ethnicity.aspx">https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/COVID-19/Race-Ethnicity.aspx</a></li>
</ul>
Note: Some race data were empty (will show as Data Not Available), an example of available data can be seen on date 14-22 May 2020<br>
Last Updated Data : """ + end.strftime('%d %B %Y'),
width=1000, height=150)




#x = np.array(data['date'],dtype=np.datetime64)
#y = np.array(data['new_confirmed_cases'])
line_df = pd.DataFrame({'x':data['date_time'], 'y':data['new_confirmed_cases']})
source = ColumnDataSource(line_df)

dataRaceSelected = getDataRaceSelected(selectedDate, selected)
pie_df=pd.DataFrame({'race':dataRaceSelected['race'], 'percentage':dataRaceSelected['percentage'], 'angle':dataRaceSelected['angle'], 'color': dataRaceSelected['color'], 'total': dataRaceSelected['total']})
pieSource = ColumnDataSource(pie_df)
    
bokeh_doc = curdoc()

lineFig = figure(plot_height=400, plot_width=700, y_axis_label='Number of Cases/Deaths',
    x_axis_type="datetime")
linePlot = lineFig.line('x', 'y', source=source)#.line(x, y)

#num_days = ((end - start) / np.timedelta64(1, 'D')).astype(int)
lineFig.xaxis.ticker = DaysTicker(
  days=np.arange(1, (end - start).days, 14)#, num_minor_ticks=6
  )

lineFig.add_tools(HoverTool(
    tooltips=[
        ('date', '@x{%Y-%m-%d}'),
        ("new cases/deaths", "@y"),
    ],

    formatters={
        '@x': 'datetime',
    }
))

lineTitle = Title()
lineTitle.text = "Coronavirus New " + selected + " Tracker"
lineFig.title = lineTitle

pieTitle = Title()
pieTitle.text = "Race Percentage in comparison to Total Population of " + selected + " (" + selectedDate + ")"

pieFig = figure(plot_height=350, toolbar_location=None, tools="hover", tooltips=("Race @race: @total{0,0} (@percentage{:.0%})"))
pieFig.title = pieTitle

piePlot = pieFig.wedge(x=0, y=1, radius=0.4, start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'), line_color="white", fill_color='color', legend_field='race', source=pieSource)

pieFig.axis.axis_label=None
pieFig.axis.visible=False
pieFig.grid.grid_line_color = None


def date_callback(attrname, old, new):      
    selected = select.value
    selectedDate = date_picker.value
    extra = ""
    
    #print("date : " + str(new) + "; select :" + selected)    
    dRaceSelected = getDataRaceSelected(selectedDate, selected)
    if dataRace.loc[dataRace['date_time'] == selectedDate].empty:
        extra = " - Data Not Available"
    
    piePlot.data_source.data = pd.DataFrame({'race':dRaceSelected['race'], 'percentage':dRaceSelected['percentage'], 'angle':dRaceSelected['angle'], 'color': dRaceSelected['color'], 'total': dRaceSelected['total']})
    '''
    piePlot.data_source.data['color']=dRaceSelected['color']
    piePlot.data_source.data['race']=dRaceSelected['race']    
    piePlot.data_source.data['percentage']=dRaceSelected['percentage']
    piePlot.data_source.data['angle']=dRaceSelected['angle']
    '''    
    pieTitle.text = "Race Percentage in comparison to Total Population of " + selected + " (" + selectedDate + ")" + extra
    pieFig.title = pieTitle     
    
    dd = date.fromisoformat(selectedDate)
    lineFig.x_range.start = datetime(dd.year, dd.month, dd.day)
    lineTitle.text = "Coronavirus New " + selected + " Tracker"
    lineFig.title = lineTitle
    
def select_callback(attrname, old, new):
    selected = select.value
    selectedDate = date_picker.value
    
    #print("select : " + new + "; date : "+ str(selectedDate))    
    
    if selected=='Cases':
        linePlot.data_source.data['y'] = data['new_confirmed_cases']               
    elif selected == 'Deaths':
        linePlot.data_source.data['y'] = data['new_deaths']
               
    date_picker.value = start.strftime('%Y-%m-%d')
    date_picker.value = selectedDate
    #date_picker.trigger('value', start.strftime('%Y-%m-%d'), selectedDate)  
    
'''
callbackPlot = CustomJS(args=dict(lineFig=lineFig), code="""
    var a = cb_obj.value;
    lineFig.x_range.start = Date.parse(a);
""")
'''


select = Select(title="Option:", value="Cases", options=["Cases", "Deaths"])
select.on_change("value", select_callback)

date_picker = DatePicker(title='Select date (data will be shown at the most left part of graph)', value=start.strftime('%Y-%m-%d'), min_date="2020-01-01", max_date="2020-10-31")
#date_picker.js_on_change('value', callbackPlot)
date_picker.on_change('value', date_callback)

#button = Button(label="Generate", button_type="success")
#button.on_click(button_callback)
'''
def update(source=source, slider=slider, window=None):
    data = source.data
    data['end'][0] = slider.value
    source.trigger('change')

slider.js_on_change('value', CustomJS.from_py_func(update))
'''

bokeh_doc.add_root(column([div, select, date_picker, row([lineFig, pieFig])]))
bokeh_doc.title = "Bokeh App"

date_picker.value = selectedDate
#date_picker.trigger('value', start.strftime('%Y-%m-%d'), selectedDate)