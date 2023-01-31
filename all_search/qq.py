def params(obj):
    import requests
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": obj,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        # обработка ошибочной ситуации
        pass

    # Преобразуем ответ в json-объект
    json_response = response.json()
    print(json_response)
    # Получаем первый топоним из ответа геокодера.
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    tp = [list(map(float, toponym['boundedBy']['Envelope'][i].split())) for i in toponym['boundedBy']['Envelope']]
    dx = str(abs(tp[0][0] - tp[1][0]))
    dy = str(abs(tp[0][1] - tp[1][1]))

    # Собираем параметры для запроса к StaticMapsAPI:
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([dx, dy]),
        "l": "map",
        "z": "2",
        "pt": f"{toponym['Point']['pos'].replace(' ', ',')},round"
    }
    return map_params
