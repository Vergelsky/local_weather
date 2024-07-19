import os

import requests


def get_weather_from_weatherapi(city):
    """
    Возвращает словарь - текущую погоду и прогноз на 1 день
    :param city: название населённого пункта
    :return: словарь {'current': ..., 'forecast': ...}
    """
    WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")

    url = f'http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={city}&days=1&aqi=no&alerts=no'

    try:
        response = requests.get(url)
    except Exception as e:
        return {'error': {'code': -1, 'message': str(e)}}

    return response.json()
