import json

from django.shortcuts import render
from django.http import JsonResponse

from local_weather.models import City
from local_weather.servises import get_weather_from_weatherapi

CONDITIONS = {1000: 'Ясно', 1003: 'Переменная облачность', 1006: 'Облачно', 1009: 'Пасмурно', 1030: 'Дымка',
              1063: 'Местами дождь', 1066: 'Местами снег', 1069: 'Местами дождь со снегом',
              1072: 'Местами замерзающая морось', 1087: 'Местами грозы', 1114: 'Поземок', 1117: 'Метель',
              1135: 'Туман', 1147: 'Переохлажденный туман', 1150: 'Местами слабая морось',
              1153: 'Слабая морось', 1168: 'Замерзающая морось', 1171: 'Сильная замерзающая морось',
              1180: 'Местами небольшой дождь', 1183: 'Небольшой дождь', 1186: 'Временами умеренный дождь',
              1189: 'Умеренный дождь', 1192: 'Временами сильный дождь', 1195: 'Сильный дождь',
              1198: 'Слабый переохлажденный дождь', 1201: 'Умеренный или сильный переохлажденный дождь',
              1204: 'Небольшой дождь со снегом', 1207: 'Умеренный или сильный дождь со снегом',
              1210: 'Местами небольшой снег', 1213: 'Небольшой снег', 1216: 'Местами умеренный снег',
              1219: 'Умеренный снег', 1222: 'Местами сильный снег', 1225: 'Сильный снег',
              1237: 'Ледяной дождь', 1240: 'Небольшой ливневый дождь',
              1243: 'Умеренный или сильный ливневый дождь', 1246: 'Сильные ливни',
              1249: 'Небольшой ливневый дождь со снегом',
              1252: 'Умеренные или сильные ливневые дожди со снегом', 1255: 'Небольшой снег',
              1258: 'Умеренный или сильный снег', 1261: 'Небольшой ледяной дождь',
              1264: 'Умеренный или сильный ледяной дождь',
              1273: 'В отдельных районах местами небольшой дождь с грозой',
              1276: 'В отдельных районах умеренный или сильный дождь с грозой',
              1279: 'В отдельных районах местами небольшой снег с грозой',
              1282: 'В отдельных районах умеренный или сильный снег с грозой'}


# Create your views here.


def index(request):
    city_history = request.COOKIES.get('city_history')

    last_city = json.loads(city_history)[-1] if city_history else ''
    last_ten_cities = json.loads(city_history)[-10:] if city_history else []

    context = {
        'title': "Местная погода",
        'last_city': last_city,
        'last_ten_cities': last_ten_cities[::-1]
    }

    return render(request, 'local_weather/index.html', context)


def get_weather(request):
    # Получаем историю запросов
    city_history = request.COOKIES.get('city_history')
    city_history = json.loads(city_history) if city_history else []

    city = request.GET.get('city')

    # Добавляем в историю запросов текущий запрос
    city_history.append(city)

    # Получаем данные о погоде
    weather_dict = get_weather_from_weatherapi(city)

    # Если от сервиса пришёл ответ с ошибкой 1006 - город не найден, возвращаем ошибку
    # Если код -1 - не удалось подключиться к сервису
    if weather_dict.get('error'):
        error_code = weather_dict['error']['code']
        match error_code:
            case 1006:
                return JsonResponse({'error': 'no_city'})
            case -1:
                return JsonResponse({'error': 'bad_connection'})
    # Увеличиваем счётчик просмотров города
    city_to_count = City.objects.filter(name=city).first()
    if city_to_count:
        city_to_count.count += 1
        city_to_count.save()
    else:
        City.objects.create(name=city, count=1)

    current_condition_code = weather_dict['current']['condition']['code']
    current_condition = CONDITIONS[current_condition_code]
    current_temp = weather_dict['current']['temp_c']

    forecast_condition_code = weather_dict['forecast']['forecastday'][0]['day']['condition']['code']
    forecast_condition = CONDITIONS[forecast_condition_code]
    forecast_temp = weather_dict['forecast']['forecastday'][0]['day']['avgtemp_c']

    data = {
        'weather': f"В городе {city} сейчас:<br>"
                   f"температура воздуха {current_temp}°C, {current_condition}.<br>"
                   f"В течении суток ожидается:<br>"
                   f"температура воздуха {forecast_temp}°C, {forecast_condition}.",
    }

    response = JsonResponse(data)
    # Сохраняем у клиента историю его запросов
    response.set_cookie('city_history', json.dumps(city_history))
    return response


def cities_report(request):
    cities = City.objects.all().values_list('name', 'count')
    report = {city: count for city, count in cities}
    return JsonResponse(report)
