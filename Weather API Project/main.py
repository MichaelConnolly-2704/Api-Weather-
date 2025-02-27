import requests
import datetime as dt

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "70fc36b24b9d8ae99362634c1aad0779"
CITY = "Cyprus"


url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY


response = requests.get(url).json()


def convert_temp(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit


temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = convert_temp(temp_kelvin)

feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = convert_temp(feels_like_kelvin)


wind_speed = response['wind']['speed']
humidity = response['main']['humidity']


description = response['weather'][0]['description']


sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

# Printing the results
print(f"Temperature in {CITY}: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
print(f"Feels like in {CITY}: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind Speed in {CITY}: {wind_speed} m/s")
print(f"General Weather in {CITY}: {description}")
print(f"Sun rises in {CITY} at {sunrise_time} local time")
print(f"Sun sets in {CITY} at {sunset_time} local time")




