FROM python:3

RUN mkdir california-coronavirus-data

WORKDIR california-coronavirus-data

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5006