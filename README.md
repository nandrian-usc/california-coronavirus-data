# California Covid-19 Case Tracker


## Project Description

Case Tracker designed to visualize California state Covid-19 new cases and deaths. The program implemented using Bokeh library and run with Bokeh server. There are 2 charts being shown:
- Line chart to show daily new cases/deaths of Covid-19 in California state
- Pie chart to show total cases/deaths in proportion to ethnicity/race.




## Files added

1. requirements.txt contain environment requirement that would create separate environment under "env" folder.

2. case_tracker.py contain main visualization script that would visualize all charts using Bokeh.

3. Dockerfile contain docker setting that would create docker image in local machine.

4. NonlocalDockerfile contain docker setting that would create docker image in non local machine such as play-with-docker labs site.

5. Existing data file used for Line Chart (new cases or deaths in California State) : cdph-state-totals.csv

6. Existing data file used for Pie Chart (total cases/deaths according to ethnicity) : cdph-race-ethnicity.csv




## Preparing Environment and Running Project

1. Open command line/power shell and do git clone by running:

```
git clone https://github.com/nandrian-usc/california-coronavirus-data.git
```

and get inside california-coronavirus-data folder:

```
cd california-coronavirus-data
```


2. If not installed yet, do pip installation of virtualenv

```
pip install virtualenv
```

3. Make new environment named "env" by running in command line:

```
python -m venv env
```

4. Activate environment by running:

```
.\env\Script\activate
```

5. Install dependencies (numpy, pandas, bokeh) with two ways:

a. by manually running in order:

```
pip install numpy
```

```
pip install pandas
```

```
pip install bokeh
```

b. Or by using requirement.txt from git clone, run:

```
pip install -r requirements.txt
```

6. Run visualization script by executing: 

```
bokeh serve --show .\case_tracker.py
```

Wait until page is opened in browser or open <a href="http://localhost:5006/case_tracker">http://localhost:5006/case_tracker</a>

7. Browse data in the charts by selecting from dropdown and date picker.

8. Shutdown bokeh server when finished by pressing Ctrl+C in terminal. Deactivate "env" environment when finished

```
deactivate
``` 





## Run Project using Docker

There are two options to build and run Dockerfile which are running it in local computer or running it in play-with-docker.

### a. Local Computer

Build in local computer and run the image will run the application bokeh server right from start so that user can just open the URL link (mentioned in powershell, ex: http://localhost:5006/case_tracker) in the browser.

i. Make sure you have docker service installed and running in your local computer. For example in this project, Docker Desktop was already running in Windows machine. Open windows PowerShell and start typing below commands.

ii. git clone github repository by running: 

```
git clone https://github.com/nandrian-usc/california-coronavirus-data.git
```

iii. Go into california-coronavirus-data folder:

```
cd california-coronavirus-data
```

iv. Build docker image using Dockerfile with prefered image name, in this case "californiacovidcasetracker"

```
docker build . -t californiacovidcasetracker
```

v. Check that image was successfully created, run:
 
```
docker images -a
``` 

See that image californiacovidcasetracker is among the result.

vi. Run docker image in container by executing:

```
docker run --rm -it -d -p 5006:5006/tcp californiacovidcasetracker:latest
```

vii. Open the Case Tracker site by opening in browser <a href="http://localhost:5006/case_tracker">http://localhost:5006/case_tracker</a>



### b. Play-With-Docker
Different docker file (named NonlocalDockerfile) was used to build image outside local Computer such as play-with-docker lab. This is because after running the created docker image, it won't run the bokeh server yet because there'll be extra configuration (which is --allow-websocket-origin) needed for networking access that should be executed in container's command line along with bokeh server command.

i. Open play-with-docker site at <a href="https://labs.play-with-docker.com/">here</a> and click Start.

ii. git clone github repository by running: 

```
git clone https://github.com/nandrian-usc/california-coronavirus-data.git
```

iii. Go into california-coronavirus-data folder:

```
cd california-coronavirus-data
```

iv. Build docker image using Dockerfile with prefered image name, in this case "californiacovidcasetracker"

```
docker build -t californiacovidcasetracker -f NonlocalDockerfile .
```

v. Check that image was successfully created, run:
 
```
docker images -a
``` 

See that image californiacovidcasetracker is among the result.

vi. Run docker image in container by executing:

```
docker run --rm -it -d -p 5006:5006/tcp californiacovidcasetracker:latest
```

vii. Before running the application, you will need information on "container name" and "playwithdocker_network_address" which can be known by:

- <container_name> : run "docker ps" command and look for the name under header NAMES, example: "gracious_ardinghelli"

- <playwithdocker_network_address> : copy ssh link under SSH field; removed "ssh " text; replace "@" text with "-5006." where 5006 is the port. 

Example from ssh copy text "ssh ip172-18-0-33-buh1nlpqckh000enmm7g@direct.labs.play-with-docker.com" then should be changed into "ip172-18-0-33-buh1nlpqckh000enmm7g-5006.direct.labs.play-with-docker.com"

viii. Execute:

```
docker exec -it <container name> bokeh serve --show ./case_tracker.py --allow-websocket-origin=<playwithdocker_network_address>
```

with first changing <container_name> and <playwithdocker_network_address> to use our respective values from step vii, or by using our previous example then the command would be:

```
docker exec -it gracious_ardinghelli bokeh serve --show ./case_tracker.py --allow-websocket-origin=ip172-18-0-33-buh1nlpqckh000enmm7g-5006.direct.labs.play-with-docker.com
```

ix. Open the Case Tracker site by clicking port link next to Open Port button (in this case: "5006")


### Misc:

i. "REPOSITORY" and "IMAGE_ID" used below can be known by executing: 

```
docker images -a
``` 

From result see under header REPOSITORY and IMAGE_ID. 

"NAMES" below can be known by executing 

```
docker ps
```

From result see under NAMES header.

ii. Stop all running containers by executing:

``` 
docker stop $(docker ps -aq)
```

or to just stop one container by executing:

``` 
docker stop <NAMES>
```

example:

```
docker stop c336566b44e3
```

iii. Save image into offline tar file by executing:

```
docker save -o <output_path> <REPOSITORY>
```

example: 

```
docker save -o D:\californiacovidcasetracker.tar californiacovidcasetracker
```

iv. Load image from offline image file by executing:

```
docker load -i <input_path> 
```

example:

```
docker load -i D:\californiacovidcasetracker.tar
```

v. Delete image by executing: 

```
docker rmi <IMAGE_ID>
```

example:

```
docker rmi b6cefbebfaaa
```

vii. See images which is dangling:

```
docker images -f dangling=true
```


# california-coronavirus-data

The Los Angeles Times' independent tally of coronavirus cases in California.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/datadesk/california-coronavirus-data/master?urlpath=lab/tree/notebooks/examples.ipynb)
![Jupyer Notebook tests](https://github.com/datadesk/california-coronavirus-data/workflows/Jupyer%20Notebook%20tests/badge.svg)

## Table of contents

- [latimes-agency-totals.csv](#latimes-agency-totalscsv)
- [latimes-county-totals.csv](#latimes-county-totalscsv)
- [latimes-state-totals.csv](#latimes-state-totalscsv)
- [latimes-agency-websites.csv](#latimes-agency-websitescsv)
- [latimes-place-totals.csv](#latimes-place-totalscsv)
- [cdph-state-totals.csv](#cdph-state-totalscsv)
- [cdph-positive-test-rate.csv](#cdph-positive-test-ratecsv)
- [cdph-age.csv](#cdph-agecsv)
- [cdph-race-ethnicity.csv](#cdph-race-ethnicitycsv)
- [cdph-skilled-nursing-totals.csv](#cdph-skilled-nursing-totalscsv)
- [cdph-adult-and-senior-care-totals.csv](#cdph-skilled-nursing-totalscsv)
- [cdph-skilled-nursing-facilities.csv](#cdph-skilled-nursing-facilitiescsv)
- [cdph-adult-and-senior-care-facilities.csv](#cdph-adult-and-senior-care-facilitiescsv)
- [cdph-nursing-home-county-totals.csv](#cdph-nursing-home-county-totalscsv)
- [cdph-hospital-patient-county-totals.csv](#cdph-hospital-patient-county-totalscsv)
- [cdph-reopening-tiers.csv](#cdph-reopening-tierscsv)
- [cdph-reopening-metrics.csv](#cdph-reopening-metricscsv)
- [cdcr-state-totals.csv](#cdcr-state-totalscsv)
- [cdcr-prison-totals.csv](#cdcr-prison-totalscsv)
- [latimes-project-roomkey-totals.csv](#latimes-project-roomkey-totalscsv)
- [latimes-beach-closures-county-list.csv](#latimes-beach-closures-county-listcsv)
- [latimes-beach-closures-area-list.csv](#latimes-beach-closures-area-listcsv)
- [los-angeles-countywide-statistical-areas.json](#los-angeles-countywide-statistical-areasjson)

## About the data

These files come from a continual Times survey of California's 58 county health agencies and three city agencies. Updated numbers are published throughout the day at [latimes.com/coronavirustracker](https://www.latimes.com/projects/california-coronavirus-cases-tracking-outbreak/). This repository will periodically update with an extract of that data.

The figures are typically ahead of the totals compiled by California's Department of Public Health. By polling local agencies, The Times database also gathers some information not provided by the state. The system has [won praise](https://twitter.com/palewire/status/1243329930877788160) from public health officials, who do not dispute its method of data collection.

The tallies here are mostly limited to residents of California, the standard method used to count patients by the state’s health authorities. Those totals do not include people from other states who are quarantined in California, such as the passengers and crew of the Grand Princess cruise ship that docked in Oakland.

## Reusing the data

The Los Angeles Times is making coronavirus infections data available for use by researchers and scientists to aid in the fight against COVID-19.

The company's Terms of Service apply. By using the data, you accept and agree to follow the [Terms of Services](https://www.latimes.com/terms-of-service).

It states that "you may use the content online only, and solely for your personal, non-commercial use, provided you do not remove any trademark, copyright or other notice from such Content," and that, "no other use is permitted without prior written permission of Los Angeles Times."

Reselling the data is forbidden. Any use of these data in published works requires attribution to the Los Angeles Times.

To inquire about reuse, please contact Data and Graphics Editor Ben Welsh at [ben.welsh@latimes.com](mailto:ben.welsh@latimes.com).

## Examples of reuse

- [UC San Francisco: "UCSF Health Atlas"](http://healthatlas.ucsf.edu/welcome)
- [UCLA: "COVID-19 Sandbox Maproom"](https://sandbox.idre.ucla.edu/covid19/?geo=la)
- [Capradio: "Track COVID-19 Cases In California By County"](https://www.capradio.org/articles/2020/03/31/track-covid-19-cases-in-california-by-county/)
- [Race Counts: "How race, class and place fuel a pandemic"](https://www.racecounts.org/covid/)
- [covid-19-datasette](https://covid-19.datasettes.com/covid)
- [KQED: "How Many Coronavirus Cases Are in California? See Latest Numbers by County"](https://www.kqed.org/news/11809760/how-many-california-coronavirus-cases-see-latest-numbers-by-county)
- [KQED: "Here Are the Trendlines for COVID-19 Deaths and Hospitalizations in Each Bay Area County"](https://www.kqed.org/science/1964968/charts-the-bay-area-is-opening-up-again-heres-tracking-data-for-each-county-to-see-how-its-going)
- [Geography Planet: Southern California COVID trend map](https://geographyplanet.org/map-gallery/southern-california-covid-19-trend-map/)
- [weylunlee.github.io/covidtrack](https://weylunlee.github.io/covidtrack/)

## Data dictionary

### [latimes-agency-totals.csv](./latimes-agency-totals.csv)

The total cases and deaths logged by local public health agencies each day. Each row contains the cumulative totals reported by a single agency as of that date.

Most counties have only one agency except for Alameda and Los Angeles counties, where some cities run independent health departments. In Alameda County, the city of Berkeley is managed independently. In Los Angeles County, Pasadena and Long Beach are managed independently. These cities' totals are broken out into separate rows. In order to calculate county-level totals, you must aggregate them together using the `county` field.

| field             | type    | description                                                                                                                                                                                                                         |
| :---------------- | :------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agency`          | string  | The name of the county or city public health agency that provided the data. Guaranteed to be unique when combined with the `date` field.                                                                                            |
| `county`          | string  | The name of the county where the agency is based.                                                                                                                                                                                   |
| `fips`            | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the `county` by the federal government. Can be used to merge with other data sources.                                              |
| `date`            | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                                                                                 |
| `confirmed_cases` | integer | The cumulative number of confirmed coronavirus cases as of this `date`.                                                                                                                                                             |
| `deaths`          | integer | The cumulative number of deaths attributed to coronavirus as of this `date`.                                                                                                                                                        |
| `recoveries`      | integer | The cumulative number of recovered cases as of this `date`. Only some agencies provide this data.                                                                                                                                   |
| `did_not_update`  | boolean | Indicates if the agency did not provide an update on this date. If this is `true` and the case and death totals are unchanged from the previous day, this means they were holdovers. Use this flag omit these records when desired. |

### [latimes-county-totals.csv](./latimes-county-totals.csv)

The county-level totals of cases and deaths logged by local public health agencies each day. This is a derived table. Each row contains the aggregation of all local agency reports in that county logged by Los Angeles Times reporters and editors in `latimes-agency-totals.csv`.

It comes with all of the same caveats as its source. It is included here as a convenience.

| field                 | type    | description                                                                                                                                                                            |
| --------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `county`              | string  | The name of the county where the agency is based.                                                                                                                                      |
| `fips`                | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the `county` by the federal government. Can be used to merge with other data sources. |
| `date`                | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                                    |
| `confirmed_cases`     | integer | The cumulative number of confirmed coronavirus case at that time.                                                                                                                      |
| `deaths`              | integer | The cumulative number of deaths at that time.                                                                                                                                          |
| `new_confirmed_cases` | integer | The net change in confirmed cases over the previous `date`.                                                                                                                            |
| `new_deaths`          | integer | The net change in deaths over the previous `date`.                                                                                                                                     |

### [latimes-state-totals.csv](./latimes-state-totals.csv)

The statewide total of cases and deaths logged by local public health agencies each day. This is a derived table. Each row contains the aggregation of all local agency reports logged by Los Angeles Times reporters and editors in `latimes-agency-totals.csv`.

It comes with all of the same caveats as its source. It is included here as a convenience.

| field                 | type    | description                                                                                         |
| --------------------- | ------- | --------------------------------------------------------------------------------------------------- |
| `date`                | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |
| `confirmed_cases`     | integer | The cumulative number of confirmed coronavirus case at that time.                                   |
| `deaths`              | integer | The cumulative number of deaths at that time.                                                       |
| `new_confirmed_cases` | integer | The net change in confirmed cases over the previous `date`.                                         |
| `new_deaths`          | integer | The net change in deaths over the previous `date`.                                                  |

### [latimes-agency-websites.csv](./latimes-agency-websites.csv)

The 61 local-health agency websites that the Los Angeles Times consults to conduct its survey.

| field    | type   | description                                                                                                                                                                                    |
| -------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `county` | string | The name of the county where the city is located.                                                                                                                                              |
| `fips`   | string | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the county by the federal government. Can be used to merge with other data sources.           |
| `agency` | string | The name of the county or city public health agency.                                                                                                                                           |
| `url`    | string | The location of the agency's website on the World Wide Web.                                                                                                                                    |

### [latimes-place-totals.csv](./latimes-place-totals.csv)

Some counties, primarily in Southern California, break out the location of cases within their service area. The Times is gathering and consolidating these lists. Each row contains cumulative case totals reported in that area as of that date.

The following counties currently do not report cases by locality: Alpine, Colusa, Glenn, Inyo, Lake, Lassen, Mariposa, Modoc, San Benito, Sierra, Tehama and Tuolumne.

Some counties provide data by region. The locations provided by Los Angeles County correspond to the public health department's official "Countywide Statistical Areas". Locations in other counties are manually geocoded by The Times. San Francisco and Imperial counties provide data at the ZIP Code level.

Be aware that some counties have shifted the place names used over time.

In some circumstances the true total of cases is obscured. Los Angeles and Orange counties decline to provide the precise number of cases in areas with low populations and instead provide a potential range. The lowest number in the range is entered into the record in the `confirmed_cases` field and an accompanying `note` includes the set of possible values.

| field             | type    | description                                                                                                                                                                          |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `date`            | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                                  |
| `county`          | string  | The name of the county where the city is located.                                                                                                                                    |
| `fips`            | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the county by the federal government. Can be used to merge with other data sources. |
| `place`           | string  | The name of the city, neighborhood or other area.                                                                                                                                    |
| `confirmed_cases` | integer | The cumulative number of confirmed coronavirus case at that time.                                                                                                                    |
| `note`            | string  | In cases where the `confirmed_cases` are obscured, this explains the range of possible values.                                                                                       |
| `x`               | float   | The longitude of the `place`.                                                                                                                                                        |
| `y`               | float   | The latitude of the `place`.                                                                                                                                                         |

### [cdph-state-totals.csv](./cdph-state-totals.csv)

Totals published by the California Department of Public Health in [its daily press releases](https://www.cdph.ca.gov/Programs/OPA/Pages/New-Release-2020.aspx). Each row contains all numbers included in that day's release.

This file includes cases and deaths, the age of victims, transmission types, tests and hospitalizations. The state has stopped supplying some fields and began supplying some others over time. Deprecated fields have been maintained in this file and are noted below.

Due to bureaucratic lags, the state's totals for cases and deaths arrive slower than The Times numbers, which are generated by surveying local agencies. The state's methods for collecting testing data have struggled with [errors](https://www.latimes.com/california/story/2020-04-04/gavin-newsom-california-coronavirus-testing-task-force) and [delays](https://www.latimes.com/business/story/2020-03-30/its-taking-up-to-eight-days-to-get-coronavirus-tests-results-heres-why).

Some dates are missing because the state did not publish a press release for that day.

| field                          | type    | description                                                                                                                                                                                                  |
| :----------------------------- | :------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `date`                         | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                                                          |
| `confirmed_cases`              | integer | The cumulative number of confirmed coronavirus case at that time.                                                                                                                                            |
| `deaths`                       | integer | The cumulative number of deaths at that time.                                                                                                                                                                |
| `travel`                       | integer | The number of cases acquired while traveling. The state stopped publishing it on March 24.                                                                                                                   |
| `person_to_person`             | integer | The number of cases acquired from close contacts and family members. The state stopped publishing it on March 24.                                                                                            |
| `community_spread`             | integer | The number of cases acquired from community spread. The state stopped publishing it on March 29.                                                                                                             |
| `under_investigation`          | integer | The number of cases acquired from an unknown source. The state stopped publishing it on March 24.                                                                                                            |
| `other_causes`                 | integer | The number of cases acquired from other sources. On March 24 the state began combining this figure with travel, person-to-person and under investigation cases. On March 29 the state stopped publishing it. |
| `self_monitoring`              | integer | The number of people in a form of isolation monitored by the state. The state stopped publishing it on March 19.                                                                                             |
| `age_0_to_17`                  | integer | The number of confirmed cases involving a person between 0 and 18 years old.                                                                                                                                 |
| `age_18_to_49`                 | integer | The number of confirmed cases involving a person between 18 and 49 years old.                                                                                                                                |
| `age_50_to_64`                 | integer | The number of confirmed cases involving a person between 50 and 64 years old.                                                                                                                                |
| `age_65_and_up`                | integer | The number of confirmed cases involving a person 65 of older.                                                                                                                                                |
| `age_18_to_64`                 | integer | The number of confirmed cases involving a person between 18 and 64 years old. The state stopped publishing it on March 23.                                                                                   |
| `age_unknown`                  | integer | The number of confirmed cases involving a person of unknown age.                                                                                                                                             |
| `gender_male`                  | integer | The number of confirmed cases involving a male.                                                                                                                                                              |
| `gender_female`                | integer | The number of confirmed cases involving a female.                                                                                                                                                            |
| `gender_unknown`               | integer | The number of confirmed cases involving a a person of unknown gender.                                                                                                                                        |
| `total_tests`                  | integer | The total number of tests conducted.                                                                                                                                                                         |
| `received_tests`               | integer | The number of tests results received. The state stopped publishing this field in April 24.                                                                                                                   |
| `pending_tests`                | integer | The number of tests resuts that are still pending. The state stopped publishing this field in April 24.                                                                                                      |
| `confirmed_hospitalizations`   | integer | The total number of hospitalizations with a confirmed case of COVID-19.                                                                                                                                      |
| `confirmed_icu`                | integer | The number of ICU hospitalizations with a confirmed case of COVID-19.                                                                                                                                        |
| `suspected_hospitalizations`   | integer | The total number of hospitalizations with a suspected case of COVID-19.                                                                                                                                      |
| `suspected_icu`                | integer | The number of ICU hospitalizations with a suspected case of COVID-19.                                                                                                                                        |
| `healthcare_worker_infections` | integer | The total number of healthcare workers who have tested positive for COVID-19.                                                                                                                                |
| `healthcare_worker_deaths`     | integer | The total number of healthcare workers who have died from COVID-19.                                                                                                                                          |
| `source_url`                   | string  | The URL to the state press release.                                                                                                                                                                          |

### [cdph-positive-test-rate.csv](./cdph-positive-test-rate.csv)

All of the data used by The Times to estimate how many recent tests have come back positive. The daily tallies of new cases and tests are drawn from [cdph-state-totals.csv](./cdph-state-totals.csv).

| field                                  | type    | description                                                                                                                                            |
| -------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `date`                                 | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                    |
| `confirmed_cases`                      | integer | The cumulative number of confirmed coronavirus case at that time.                                                                                      |
| `total_tests`                          | integer | The total number of tests conducted.                                                                                                                   |
| `new_confirmed_cases`                  | integer | The number of new confirmed cases compared to the previous date.                                                                                       |
| `new_tests`                            | integer | The number of new tests compared to the previous date.                                                                                                 |
| `new_confirmed_cases_seven_day_total`  | integer | The total number of new confirmed cases in the previous seven days.                                                                                    |
| `new_tests_seven_day_total`            | integer | The total number of new tests in the previous seven days.                                                                                              |
| `positive_test_rate_seven_day_percent` | float   | The positive test rate over the past seven days, calculated by dividing the number of new confirmed cases over that time into the number of new tests. |

### [cdph-age.csv](./cdph-age.csv)

Statewide demographic data tallying totals by age for both cases and deaths. Provided by the [California Department of Public Health](https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/COVID-19/COVID-19-Cases-by-Age-Group.aspx).

| field                     | type    | description                                                                                         |
| ------------------------- | ------- | --------------------------------------------------------------------------------------------------- |
| `date`                    | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |
| `age`                     | string  | The age bracket being tallied                                                                       |
| `confirmed_cases_total`   | integer | The cumulative number of confirmed coronavirus case amoung this age bracket at that time.           |
| `confirmed_cases_percent` | float   | The case totals percentage of the total in this age bracket                                         |
| `deaths_total`            | integer | The cumulative number of deaths case amoung this age bracket at that time.                          |
| `deaths_percent`          | float   | The death totals percentage of the total in this age bracket.                                       |

### [cdph-race-ethnicity.csv](./cdph-race-ethnicity.csv)

Statewide demographic data tallying race totals by age for both cases and deaths. Provided by the [California Department of Public Health](https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/COVID-19/Race-Ethnicity.aspx).

The original race categories published by the state have been grouped and aggregated to match the five race categories traditionally published by the Los Angeles Times.

| field                     | type    | description                                                                                         |
| ------------------------- | ------- | --------------------------------------------------------------------------------------------------- |
| `date`                    | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |
| `race`                    | string  | The race being tallied.                                                                             |
| `age`                     | string  | The age bracket being tallied                                                                       |
| `confirmed_cases_total`   | integer | The cumulative number of confirmed coronavirus case amoung this race and age at that time.          |
| `confirmed_cases_percent` | float   | The case totals percentage of the total in this age bracket                                         |
| `deaths_total`            | integer | The cumulative number of deaths case amoung this race and age at that time.                         |
| `deaths_percent`          | float   | The death totals percentage of the total in this age bracket.                                       |
| `population_percent`      | float   | The race's percentage of the overall state population in this age bracket.                          |

### [cdph-skilled-nursing-totals.csv](./cdph-skilled-nursing-totals.csv)

California's Department of Public Health is releasing totals tracking the cumulative number of cases and deaths at the state's skilled nursing facilities.

In some circumstances the true total of cases is obscured. The lowest number in the range is entered into the record in the staff or patients field and an accompanying `note` field includes the set of possible values.

| field                           | type    | description                                                                                             |
| ------------------------------- | ------- | ------------------------------------------------------------------------------------------------------- |
| `date`                          | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.     |
| `staff_active_cases`            | integer | The number of active coronavirus case among staff at that time.                                         |
| `patients_active_cases`         | integer | The number of active coronavirus case amoung patients at that time.                                     |
| `staff_confirmed_cases`         | integer | The cumulative number of confirmed coronavirus case among staff at that time.                           |
| `patients_confirmed_cases`      | integer | The cumulative number of confirmed coronavirus case among patients at that time.                        |
| `staff_deaths`                  | integer | The cumulative number of deaths case among staff at that time.                                          |
| `patients_deaths`               | integer | The cumulative number of deaths case among patients at that time.                                       |
| `staff_deaths_note`             | string  | In cases where the `staff_deaths` are obscured, this explains the range of possible values.             |
| `source_url`                    | string  | The URL to the state data release.                                                                      |

### [cdph-adult-and-senior-care-totals.csv](./cdph-adult-and-senior-care-totals.csv)

California's Department of Social Services is releasing totals tracking the cumulative number of cases and deaths at the state's residential care facilities for the elderly and adult residential facilities. The source documents are available in the [pdf/adult-and-senior-care/](pdf/adult-and-senior-care/) directory of this repository.

These are also sometimes known as assisted-living facilities. Counts for staff and patients are combined in this dataset into a single total.

| field             | type    | description                                                                                         |
| ----------------- | ------- | --------------------------------------------------------------------------------------------------- |
| `date`            | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |
| `confirmed_cases` | integer | The cumulative number of confirmed coronavirus case amoung staff and patients at that time.         |
| `deaths`          | integer | The cumulative number of deaths case amoung staff and patients at that time.                        |
| `active_cases`    | integer | The number of active coronavirus case at that time.                                                 |
| `source_url`      | string  | The URL to the state data release.                                                                  |

### [cdph-skilled-nursing-facilities.csv](./cdph-skilled-nursing-facilities.csv)

California's Department of Social Services is [listing the skilled-nursing facilities](https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/COVID-19/SNFsCOVID_19.aspx) across the state with COVID-19 outbreaks. The source documents are available in the [pdf/adult-and-senior-care/](pdf/adult-and-senior-care/) directory of this repository.

In some circumstances the true total of cases is obscured. The lowest number in the range is entered into the record in the staff or patients field and an accompanying `note` field includes the set of possible values.

| field                           | type    | description                                                                                                                                                                          |
| ------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `date`                          | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                                  |
| `id`                            | string  | The facility's unique identifier with the state.                                                                                                                                     |
| `name`                          | string  | The name of the skilled-nursing facility.                                                                                                                                            |
| `county`                        | string  | The name of the county where the city is located.                                                                                                                                    |
| `fips`                          | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the county by the federal government. Can be used to merge with other data sources. |
| `staff_confirmed_cases`         | integer | The current number of confirmed coronavirus case amoung staff at that time.                                                                                                          |
| `patients_confirmed_cases`      | integer | The current number of confirmed coronavirus case amoung patients at that time.                                                                                                       |
| `staff_confirmed_cases_note`    | string  | In cases where the `staff_confirmed_cases` are obscured, this explains the range of possible values.                                                                                 |
| `patients_confirmed_cases_note` | string  | In cases where the `patients_confirmed_cases` are obscured, this explains the range of possible values.                                                                              |
| `staff_deaths`                  | integer | The cumulative number of deaths case amoung staff at that time.                                                                                                                      |
| `patients_deaths`               | integer | The cumulative number of deaths case amoung patients at that time.                                                                                                                   |
| `staff_deaths_note`             | string  | In cases where the `staff_deaths` are obscured, this explains the range of possible values.                                                                                          |
| `patients_deaths_note`          | string  | In cases where the `patients_deaths` are obscured, this explains the range of possible values.                                                                                       |

### [cdph-adult-and-senior-care-facilities.csv](./cdph-residential-care-facilities.csv)

California's Department of Public Health is [listing the residential care facilities for the elderly and adult residential facilities](https://www.cdss.ca.gov/#covid19) across the state with COVID-19 outbreaks.

These are also sometimes known as assisted-living facilities. In some circumstances the true total of cases is obscured. The lowest number in the range is entered into the record in the staff or patients field and an accompanying `note` field includes the set of possible values.

| field                           | type    | description                                                                                                                                                                          |
| ------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `date`                          | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                                  |
| `name`                          | string  | The name of the nursing home.                                                                                                                                                        |
| `county`                        | string  | The name of the county where the city is located.                                                                                                                                    |
| `fips`                          | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the county by the federal government. Can be used to merge with other data sources. |
| `staff_confirmed_cases`         | integer | The cumulative number of confirmed coronavirus case amoung staff at that time.                                                                                                       |
| `patients_confirmed_cases`      | integer | The cumulative number of confirmed coronavirus case amoung patients at that time.                                                                                                    |
| `staff_confirmed_cases_note`    | string  | In cases where the `staff_confirmed_cases` are obscured, this explains the range of possible values.                                                                                 |
| `patients_confirmed_cases_note` | string  | In cases where the `patients_confirmed_cases` are obscured, this explains the range of possible values.                                                                              |
| `staff_deaths`                  | integer | The cumulative number of deaths amoung staff at that time.                                                                                                                      |
| `patients_deaths`               | integer | The cumulative number of deaths amoung patients at that time.                                                                                                                   |
| `staff_deaths_note`             | string  | In cases where the `staff_deaths` are obscured, this explains the range of possible values.                                                                                          |
| `patients_deaths_note`          | string  | In cases where the `patients_deaths` are obscured, this explains the range of possible values.                                                                                       |

### [cdph-nursing-home-county-totals.csv](./cdph-nursing-home-county-totals.csv)

The total number of cases and deaths in skilled-nursing facilities, residential care facilities for the elderly and adult residential facilities aggregated by county.

These numbers are calculated by The Times using the facilities lists above. The state chooses not to provide precise numbers at facilities with fewer than 10 cases. When totaling by county, The Times substitutes the minimum value of one. The result is that the tallies are likely an undercount and should be considered the minimum possible value.

| field                                   | type    | description                                                                                                                                                                          |
| --------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `date`                                  | date    | The date when the data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                                  |
| `county`                                | string  | The name of the county where the city is located.                                                                                                                                    |
| `fips`                                  | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the county by the federal government. Can be used to merge with other data sources. |
| `minimum_staff_confirmed_cases`         | integer | The minimum number of cumulative confirmed coronavirus case amoung staff at that time.                                                                                               |
| `minimum_patients_confirmed_cases`      | integer | The minimum number of cumulative confirmed coronavirus case amoung patients at that time.                                                                                            |
| `minimum_staff_deaths`                  | integer | The minimum number of cumulative deaths amoung staff at that time.                                                                                                                   |
| `minimum_patients_deaths`               | integer | The minimum number of cumulative deaths amoung patients at that time.                                                                                                                |

### [cdph-hospital-patient-county-totals.csv](./cdph-hospital-patient-county-totals.csv)

California's Department of Public Health is releasing [county-level hospitalization totals](https://data.chhs.ca.gov/dataset/california-covid-19-hospital-data-and-case-statistics).

| field                    | type    | description                                                                                                                                                                          |
| ------------------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `date`                   | date    | The date for which hospital data were reported in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                         |
| `county`                 | string  | The name of the county.                                                                                                                                                              |
| `fips`                   | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the county by the federal government. Can be used to merge with other data sources. |
| `positive_patients`      | integer | The current number confirmed coronavirus cases in hospitals on this `date`.                                                                                                          |
| `suspected_patients`     | integer | The current number suspected coronavirus cases in hospitals on this `date`.                                                                                                          |
| `icu_positive_patients`  | integer | The current number confirmed coronavirus cases in intensive-care units on this `date`.                                                                                               |
| `icu_suspected_patients` | integer | The current number suspected coronavirus cases in intensive-care units on this `date`.                                                                                               |
| `icu_available_beds`     | integer | The current number open and avilable intensive-care beds on this `date`.                                                                                                             |

### [cdph-reopening-tiers.csv](./cdph-reopening-tiers.csv)

In August 2020, the state introduced a new framework for deciding when and how counties can reopen. Under the regime, each county is assigned to one of four tiers based on a set of metrics developed by state officials.

This file records the current tier of each county by day. The definition for each group can be found on the [state's website](https://web.archive.org/web/20200829140027/https://covid19.ca.gov/safer-economy/).

| field    | type    | description                                                                                                                                                                          |
| -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `date`   | date    | The date when the data were collected in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                                  |
| `county` | string  | The name of the county.                                                                                                                                                              |
| `fips`   | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the county by the federal government. Can be used to merge with other data sources. |
| `tier`   | integer | The tier the county was classified in on this `date`. There are four possible values on an ordinal scale with one being the most restrictive and four the least restrictive.         |

### [cdph-reopening-metrics.csv](./cdph-reopening-metrics.csv)

In August 2020, the state introduced a new framework for deciding when and how counties can reopen. Under the regime, each county is assigned to one of four tiers based on a set of metrics developed by state officials.

This file records the metrics recorded for each county by day. Definition of the benchmarks can be found on the [state's website](https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/COVID-19/COVID19CountyMonitoringOverview.aspx).

| field                 | type    | description                                                                                                                                                                          |
| --------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `date`                | date    | The date when the data were collected in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                                  |
| `county`              | string  | The name of the county.                                                                                                                                                              |
| `fips`                | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the county by the federal government. Can be used to merge with other data sources. |
| `percapita_case_rate` | float   | The number of new cases in a recent seven-day period — excluding cases at prisons and jails — adjusted for population and multiplied by 100,000.                                     |
| `adjusted_case_rate`  | float   | The `percapita_case_rate` adjusted to account for the volume of testing in the area. Not done for all counties.                                                                      |
| `positivity_rate`     | float   | The percentage of tests for the virus that come back positive in a recent seven-day period.                                                                                          |
| `equity_metric`       | float   | An index measuring disparities in disadvantaged neighborhoods compared to the county overall. Many small counties are exempted. Added Oct. 6, 2020                                   |

### [cdcr-state-totals.csv](./cdcr-state-totals.csv)

The total number of cases amoung inmates at prisons run by the California Department of Corrections and Rehabiliation.

| field                 | type    | description                                                                                         |
| --------------------- | ------- | --------------------------------------------------------------------------------------------------- |
| `date`                | date    | The date when the data were collected in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |
| `confirmed_cases`     | integer | The cumulative number of confirmed coronavirus case at that time.                                   |
| `new_confirmed_cases` | integer | The net change in confirmed cases over the previous `date`.                                         |
| `active_cases`        | integer | The number of active coronavirus case at that time.                                                 |

### [cdcr-prison-totals.csv](./cdcr-prison-totals.csv)

The cases, resolutions and deaths among inmates at the individual prison facilities operated by the California Department of Corrections and Rehabilitation.

The data is currently limited to July 22, 2020, forward.

| field                 | type    | description                                                                                                                                                                          |
| --------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `date`                | date    | The date when the data were collected in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                                  |
| `code`                | string  | The unique identifier of the prison institution.                                                                                                                                     |
| `name`                | string  | The name of the prison institution.                                                                                                                                                  |
| `city`                | string  | The city where the prison institution is located.                                                                                                                                    |
| `county`              | string  | The county where the prison institution is located.                                                                                                                                  |
| `fips`                | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the county by the federal government. Can be used to merge with other data sources. |
| `zipcode`             | string  | The [ZIP Code](https://en.wikipedia.org/wiki/ZIP_Code) where the agency is located.                                                                  |
| `x`                   | float   | The longitude of the area's centroid.                                                                                                                                                |
| `y`                   | float   | The latitude of the area's centroid.                                                                                                                                                 |
| `confirmed_cases`     | integer | The cumulative number of confirmed coronavirus case at that time.                                                                                                                    |
| `new_confirmed_cases` | integer | The net change in confirmed cases over the previous `date`.                                                                                                                          |
| `active_cases`        | integer | The number of active coronavirus case at that time.                                                                                                                                  |
| `released_cases`      | integer | The cumulative number of coronavirus cases released from the prison at that time.                                                                                                        |
| `resolved_cases`      | integer | The cumulative of coronavirus case where the patient ultimately recovered or had their cases otherwise resolved at that time.                                                            |
| `deaths`              | integer | The cumulative number of deaths at that time.                                                                                                                                        |
| `new_deaths`          | integer | The net change in deaths over the previous `date`.                                                                                                                                   |

### [latimes-project-roomkey-totals.csv](./latimes-project-roomkey-totals.csv)

Los Angeles County officials have launched an unprecedented effort to shield 15,000 homeless people from the coronavirus by moving them into hotel rooms. The Times is tracking the latest data from the Los Angeles County Emergency Operations Center and the Los Angeles County Department of Public Health.

| field                      | type    | description                                                                                             |
| -------------------------- | ------- | ------------------------------------------------------------------------------------------------------- |
| `date`                     | date    | The date on which data were reported in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.      |
| `people_housed`            | integer | The current number of homeless people in Los Angeles County housed on this `date`.                      |
| `leased_rooms`             | integer | The current number hotel rooms leased on this `date`.                                                   |
| `rooms_ready_to_occupy`    | integer | The subset of leased rooms that were ready to occupy on this `date`.                                    |
| `rooms_occupied`           | integer | The subset of ready rooms that were occupied on this `date`.                                            |
| `homeless_confirmed_cases` | integer | The cumulative number of homeless people in Los Angeles County that had tested positive by this `date`. |

### [latimes-beach-closures-county-list.csv](./latimes-beach-closures-county-list.csv)

The county-level restrictions on beach access, compiled by the Los Angeles Times based on data released by the California Coastal Commission.

| field         | type   | description                                                                                                                                                                            |
| ------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `county`      | string | The name of the county where the agency is based.                                                                                                                                      |
| `fips`        | string | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the `county` by the federal government. Can be used to merge with other data sources. |
| `status`      | string | A Times classification of the current level of restriction in this county                                                                                                              |
| `restriction` | string | A description of the current level of restriction in this county                                                                                                                       |

### [latimes-beach-closures-area-list.csv](./latimes-beach-closures-area-list.csv)

The subcounty-level restrictions on beach access, compiled by the Los Angeles Times based on data released by the California Coastal Commission.

| field         | type    | description                                                                                                                                                                            |
| ------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `county`      | string  | The name of the county where the agency is based.                                                                                                                                      |
| `fips`        | string  | The [FIPS code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) given to the `county` by the federal government. Can be used to merge with other data sources. |
| `area`        | string  | The name of the sub-county area being tracked.                                                                                                                                         |
| `state_park`  | boolean | An indicator if this area is a state park.                                                                                                                                             |
| `restriction` | string  | A description of the current level of restriction in this area.                                                                                                                        |

### [los-angeles-countywide-statistical-areas.json](./los-angeles-countywide-statistical-areas.json)

A GeoJSON file mapping out statistical tabulation areas created by the Los Angeles County Department of Public Health. Place-level data released by Los Angeles County correspond to these areas. Acquired via a California Public Records Act request.

| field        | type    | description                                                           |
| ------------ | ------- | --------------------------------------------------------------------- |
| `type`       | string  | The type of area being mapped. Options are `City` and`Unincorporated` |
| `city`       | string  | The name of the area's municipal parent, if it has one.               |
| `community`  | string  | The name of the area.                                                 |
| `label`      | boolean | A combination of the area's name and city. Creates a unique string.   |
| `centroid_x` | float   | The longitude of the area's centroid.                                 |
| `centroid_y` | float   | The latitude of the area's centroid.                                  |

## Getting started

The data published here can be easily imported to any data analysis tool, ranging from a simple spreadsheet to a more sophisticated analysis framework. This repository has be pre-configured to work with the [Python](https://www.python.org/) computer-programming language and a [Jupyter](https://jupyter.org/) computational notebook. You can install and run the code locally on your computer, or on the web with [Binder](https://mybinder.org/).

### Installing locally

[Make a fork](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) of this repository, [clone it](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) to your computer, then move into the directory.

```
cd california-coronavirus-data
```

Install the Python tools you need with [pipenv](https://pipenv.pypa.io/en/latest/).

```
pipenv install
```

Start the Jupyter Lab programming environment.

```
pipenv run jupyter lab
```

Check out the example notebook at [notebooks/examples.ipynb](./notebooks/examples.ipynb).

### Running online with Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/datadesk/california-coronavirus-data/master?urlpath=lab/tree/notebooks/examples.ipynb)

Click on the [Binder](https://mybinder.org/) badge above and this repository will boot up inside the site's system for running Jupyter notebooks over the web. After a few minutes you should have an Jupyter Lab environment up and running.

## How you can help

This survey is conducted by The Times' Data and Graphics Department. If you'd like to support its effort to keep California and the nation informed, the best thing you can do is [buy a digital subscription](https://www.latimes.com/subscriptions/) and encourage others to do the same. The coronavirus pandemic has had a significant effect on the country's economy and the news industry is no exception. Without support from readers like you projects like this would not be possible.

## Contact

To inquire about the data or about reuse, please contact Data and Graphics Editor [Ben Welsh](https://palewi.re/who-is-ben-welsh/) at [ben.welsh@latimes.com](mailto:ben.welsh@latimes.com)
