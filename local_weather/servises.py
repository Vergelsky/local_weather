import os

import requests
import json


def get_weather_from_weatherapi(city):
    """
    Возвращает словарь - текущую погоду и прогноз на 1 день
    :param city: название населённого пункта
    :return: словарь {'current': ..., 'forecast': ...}
    """
    WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")

    url = f'http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={city}&days=1&aqi=no&alerts=no'

    response = requests.get(url)

    return response.json()
