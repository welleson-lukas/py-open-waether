
import pytest
from py_open_weather.exceptions import InvalidIPAddress
from py_open_weather.location_ip_service import LocationIPAddress
from tests.payloads import RESPONSE_SERVICE_LOCATION_INVALID_IP_ADDRESS, RESPONSE_SERVICE_LOCATION_IP_ADDRESS

URL_LOCALIZATION_IP_SERVICE = 'http://ipinfo.io/{}/json'
IP_ADDRESS = '179.234.219.226'


def test_get_location_by_ip_address(requests_mock, json_headers):
    expected_response = RESPONSE_SERVICE_LOCATION_IP_ADDRESS

    requests_mock.get(
        url=URL_LOCALIZATION_IP_SERVICE.format(IP_ADDRESS),
        status_code=200,
        headers=json_headers,
        json=expected_response
    )

    response_ip_address = LocationIPAddress.find_location_by_ip_address(
        ip_address=IP_ADDRESS)

    assert response_ip_address == f"{expected_response['city']}, {expected_response['country']}"


def test_get_location_by_ip_address_when_invalid_address(requests_mock, json_headers):
    expected_response = RESPONSE_SERVICE_LOCATION_INVALID_IP_ADDRESS

    requests_mock.get(
        url=URL_LOCALIZATION_IP_SERVICE.format(IP_ADDRESS),
        status_code=200,
        headers=json_headers,
        json=expected_response
    )
    with pytest.raises(InvalidIPAddress):
        LocationIPAddress.find_location_by_ip_address(ip_address=IP_ADDRESS)

    assert requests_mock.call_count == 1
