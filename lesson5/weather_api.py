import requests

# Checking weather in requested city.
while True:
    try:
        city_name = input('Please enter city: ')
        break
    except ValueError:
        print('Please enter a valid city name.')
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric'

response = requests.get(url)
data = response.json()
try:
    temperature = data['main']
    print(f'Current temperature in {city_name.capitalize()} is ', temperature['temp'], '°C')
    print('It feels like', temperature['feels_like'], f'°C in {city_name.capitalize()}')
except KeyError:
    print('Such city could not be found')





