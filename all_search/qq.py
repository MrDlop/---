def params(obj):
    import requests
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": obj,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        pass

    json_response = response.json()
    print(json_response)
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    tp = [list(map(float, toponym['boundedBy']['Envelope'][i].split())) for i in toponym['boundedBy']['Envelope']]
    dx = str(abs(tp[0][0] - tp[1][0]))
    dy = str(abs(tp[0][1] - tp[1][1]))

    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([dx, dy]),
        "l": "map",
        "scale": "1",
        "pt": f"{toponym['Point']['pos'].replace(' ', ',')}"
    }
    return map_params
