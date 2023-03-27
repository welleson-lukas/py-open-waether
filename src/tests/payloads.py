RESPONSE_SERVICE_OPEN_WEATHER = {
    'coord': {
        'lon': -48.5044,
        'lat': -1.4558
    },
    'weather': [
        {
            'id': 802,
            'main': 'Clouds',
            'description': 'scattered clouds',
            'icon': '03d'
        }
    ],
    'base': 'stations',
    'main': {
        'temp': 31.02,
        'feels_like': 33.7,
        'temp_min': 31.02,
        'temp_max': 31.02,
        'pressure': 1011,
        'humidity': 55
    },
    'visibility': 10000,
    'wind': {
        'speed': 2.06,
        'deg': 300
    },
    'clouds': {
        'all': 40
    },
    'dt': 1679939375,
    'sys': {
        'type': 1,
        'id': 8321,
        'country': 'BR',
        'sunrise': 1679908578,
        'sunset': 1679952146
    },
    'timezone': -10800,
    'id': 3405870,
    'name': 'Belém',
    'cod': 200
}

RESPONSE_SERVICE_OPEN_WEATHER_CITY_NOT_FOUND = {
    'cod': 404,
    'message': 'city not found'
}

RESPONSE_SERVICE_LOCATION_IP_ADDRESS = {
    'ip': '179.234.219.226',
    'hostname': 'b3eadbe2.virtua.com.br',
    'city': 'Belém',
    'region': 'Pará',
    'country': 'BR',
    'loc': '-1.4558,-48.5044',
    'org': 'AS28573 Claro NXT Telecomunicacoes Ltda',
    'postal': '66000-000',
    'timezone': 'America/Belem',
    'readme': 'https://ipinfo.io/missingauth'
}

RESPONSE_SERVICE_LOCATION_INVALID_IP_ADDRESS = {
    'ip': '192.168.0.1',
    'bogon': True
}
