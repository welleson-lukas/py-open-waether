import requests
from py_open_weather.exceptions import CityNotFound
from py_open_weather.location_ip_service import LocationIPAddress


class WeatherService:
    """
    Use of the service is conditioned to a registered account at https://openweathermap.org.
    When registering, inform the token for using the weather service.
    """

    def __init__(self, token: str) -> None:
        self.token = token

    def fetch_weather(self, city: str = None, ip_address: str = None) -> dict:
        """
        To obtain the weather, it is possible to inform or not the IP address,
        when the IP address is not provided, the public address of the network
        where the application is hosted will be adopted by default.

        Example address: 192.168.0.1

        Please provide a valid address.
        """
        
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'

        try:
            if ip_address:
                city = LocationIPAddress.find_location_by_ip_address(ip_address=ip_address)
                
            response = requests.get(url.format(city, self.token)).json()

            if response['cod'] == 404:
                raise CityNotFound
            
            return response

        except Exception as e:
            raise e

