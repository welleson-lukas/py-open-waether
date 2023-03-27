import requests

from py_open_weather.exceptions import InvalidIPAddress


class LocationIPAddress:

    @classmethod
    def find_location_by_ip_address(cls, ip_address: str = None) -> dict:
        if ip_address:
            url_service = 'http://ipinfo.io/{}/json'
        else:
            url_service = 'http://ipinfo.io/json'

        try:
            response = requests.get(url_service.format(ip_address)).json()

            if not response.get('city'):
                raise InvalidIPAddress

            return f"{response['city']}, {response['country']}"

        except Exception as e:
            raise e
