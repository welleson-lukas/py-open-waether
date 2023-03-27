<p align="center">
  <a href="#como-usar">Como Usar</a> |
  <a href="#créditos">Créditos</a>
</p>


## Como usar

*A PyOpenWeather foi desenvolvida para integração de consultas sob demandas em páginas web. A consulta de clima em massa através de *scripts* ou qualquer outros meios não é recomendada.*

A PyOpenWeather utiliza por padrão de consulta a API provida pelo serviço [OpenWeather](https://openweathermap.org/).

### Exemplo de consulta ao serviço:

Usando endereço IP:
```python
from py_open_weather import WeatherService

service = WeatherService(token='a2d4d317-c2df494d-a1ad57034b')
weather = service.fetch_weather(ip_address='192.168.0.1')
```

Usando nome da cidade:
```python
from py_open_weather import WeatherService

service = WeatherService(token='a2d4d317-c2df494d-a1ad57034b')
weather = service.fetch_weather(city='Belém, BR')
```

### Retorno e Exceptions

O formato de resposta sempre será um objeto `dict` contendo as seguintes chaves:

```python
{
    'coord': {
        'lon': 'float',
        'lat': 'float'
    },
    'weather': [
        {
            'id': 'int',
            'main': 'str',
            'description': 'str',
            'icon': 'str'
        }
    ],
    'base': 'str',
    'main': {
        'temp': 'float',
        'feels_like': 'float',
        'temp_min': 'float',
        'temp_max': 'float',
        'pressure': 'float',
        'humidity': 'float'
    },
    'visibility': 'float',
    'wind': {
        'speed': 'float',
        'deg': 'float'
    },
    'clouds': {
        'all': 'float'
    },
    'dt': 'timestemp',
    'sys': {
        'type': 'int',
        'id': 'int',
        'country': 'str',
        'sunrise': 'int',
        'sunset': 'int'
    },
    'timezone': 'float',
    'id': 'int',
    'name': 'str',
    'cod': 'int'
}
```

A PyOpenWeather tambem dá suporte a um grupo de *exceptions* que podem ser utilizadas para tratamento de quaisquer erros que ocorram durante o processo de consulta.

```python

from py_open_weather import WeatherService


try:

    service = WeatherService(token="a2d4d317-c2df494d-a1ad57034b")
    weather = service.fetch_weather(ip_address="192.168.0.1")

except exceptions.InvalidIPAddress as eiia:
    print(eiipa)

except exceptions.CityNotFound as ecnf:
    print(ecnf)

```

## Importante
O projeto PyOpenWeather foi desenvolvido para fins didáticos e infelizmente não está disponível em bibliotecas públicas para uso geral. Fique à vontade para utiliza-la em seus projetos e estudos. Abraços!

## Créditos

Copyright (C) 2023 por Welleson Lukas