import requests
import json
import datetime as dt
import calendar

url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=59.28&lon=17.54"
sitename = "www.fixit42.com, sofia@fixit42.com" # for User-Agent

session = requests.Session()
try:
    response = session.get(url, headers={"user-agent": sitename})
except (requests.exceptions.Timeout, requests.exceptions.TooManyRedirects, requests.exceptions.RequestException, requests.exceptions.ConnectionError, requests.exceptions.HTTPError) as e:
    print("No internet connection")
    exit()

if response.status_code == 200:
    yr = json.loads(response.text)
    temp_unit = yr['properties']['meta']['units']['air_temperature']
    for time in yr['properties']['timeseries']:
        dt_weather = dt.datetime.fromisoformat(time['time'])
        print(f"{dt_weather.date()} {dt_weather.strftime('%H:%M')}: {str(time['data']['instant']['details']['air_temperature'])} {temp_unit}")
