#VARUN

import requests
from datetime import datetime

api_key = '7b8c8a11b376d5fc99f1352521a9a54b'
location = input("Enter the City name : ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#Creating variables to store the data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_speed = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


print('_________________________________________________________________')
print("weather stat's for - {} || {}".format(location.upper(), date_time))
print('_________________________________________________________________')

print("Current Temperature is : {:.2f} deg C".format(temp_city))
print(f"Current weather description : {weather_desc}")
print(f"Current humidity : {hmdt} %")
print(f"Current wind speed : {wind_speed} kmph")
print('_________________________________________________________________')

txt = open('weather.txt','a')

txt.write('\n_________________________________________________________________\n')
txt.write(f"\nweather stat's for - {location.upper()}  {date_time}")
txt.write('\n_________________________________________________________________\n')

txt.write("\n Current Temperature is : {:.2f} deg C".format(temp_city))
txt.write(f"\n Current weather description : {weather_desc}")
txt.write(f"\n Current humidity : {hmdt} %")
txt.write(f"\n Current wind speed : {wind_speed} kmph")
txt.write('\n_________________________________________________________________\n')

txt.close()
