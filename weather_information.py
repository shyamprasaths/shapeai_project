
# import request module
import requests
# import date and time from os
from datetime import datetime
# import sys
import sys

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

full_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(full_api_link)
api_data = api_link.json()

# creating variables names to store and display data

tempofcity = ((api_data['main']['temp']) - 273.15)
weather_info = api_data['weather'][0]['description']
humidity = api_data['main']['humidity']
wind_speed = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


def output():
    print("-------------------------*****-------------------------------")
    print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    print("-------------------------~~~~~-------------------------------")

    print("Current temperature is: {:.2f} deg C".format(tempofcity))
    print("Current weather info  :", weather_info)
    print("Current Humidity      :", humidity, '%')
    print("Current wind speed    :", wind_speed, 'km/h')


file = open('out.txt', 'wt')

sys.stdout = file

output()

file.close()

