import sys
from io import BytesIO

import requests
from PIL import Image

from qq import params

toponym_to_find = " ".join(sys.argv[1:])

map_params = params(toponym_to_find)

map_api_server = "http://static-maps.yandex.ru/1.x/"

response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()
