import requests
from pprint import pprint
url = 'http://api.open-notify.org/astros.json'

response = requests.get(url)

requested_data = response.json()

people_in_space = requested_data['people']
print('People currently in space:')
for person in people_in_space:
    print(person['name'])
