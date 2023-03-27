from py_open_weather.exceptions import CityNotFound
import pytest

from py_open_weather.weather_service import WeatherService
from tests.payloads import RESPONSE_SERVICE_LOCATION_IP_ADDRESS, RESPONSE_SERVICE_OPEN_WEATHER_CITY_NOT_FOUND, RESPONSE_SERVICE_OPEN_WEATHER

TOKEN = '123456'
URL_WEATHER_SERVICE = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'
URL_LOCALIZATION_IP_SERVICE = 'http://ipinfo.io/{}/json'
CITY = 'Belém, BR'
IP_ADDRESS = '179.234.219.226'


def test_get_weather_by_city(requests_mock, json_headers):
    expected_response = RESPONSE_SERVICE_OPEN_WEATHER

    requests_mock.get(
        url=URL_WEATHER_SERVICE.format(CITY, TOKEN),
        status_code=200,
        headers=json_headers,
        json=expected_response
    )

    py_open_weather = WeatherService(token=TOKEN)
    response = py_open_weather.fetch_weather(city=CITY)

    assert response == expected_response


def test_get_weather_by_ip_address(requests_mock, json_headers):
    expected_response = RESPONSE_SERVICE_OPEN_WEATHER
    expected_response_ip_address = RESPONSE_SERVICE_LOCATION_IP_ADDRESS

    requests_mock.get(
        url=URL_LOCALIZATION_IP_SERVICE.format(IP_ADDRESS),
        status_code=200,
        headers=json_headers,
        json=expected_response_ip_address
    )

    requests_mock.get(
        url=URL_WEATHER_SERVICE.format(CITY, TOKEN),
        status_code=200,
        headers=json_headers,
        json=expected_response
    )

    py_open_weather = WeatherService(token=TOKEN)
    response = py_open_weather.fetch_weather(ip_address=IP_ADDRESS)

    assert response == expected_response


def test_get_weather_when_city_not_found(requests_mock, json_headers):
    expected_response = RESPONSE_SERVICE_OPEN_WEATHER_CITY_NOT_FOUND

    requests_mock.get(
        url=URL_WEATHER_SERVICE.format(CITY, TOKEN),
        status_code=404,
        headers=json_headers,
        json=expected_response
    )

    with pytest.raises(CityNotFound):
        py_open_weather = WeatherService(token=TOKEN)
        py_open_weather.fetch_weather(city=CITY)

    assert requests_mock.call_count == 1
