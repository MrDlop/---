import sys
from io import BytesIO

import requests
from PIL import Image

from qq import params

toponym_to_find = " ".join(sys.argv[1:])

map_params = params('уфа ахметова 300')

map_api_server = "http://static-maps.yandex.ru/1.x/"
geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": 'аптека',
    'results': '1',
    "format": "json",
    "ll": map_params['pt']}
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
response = requests.get(geocoder_api_server, params=geocoder_params)
json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]
toponym_coodrinates = toponym["Point"]["pos"]
ll = toponym_coodrinates.replace(" ", ',')
print(map_params['pt'])
print(ll)
map_params['pt'] += '~' + ll
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()
