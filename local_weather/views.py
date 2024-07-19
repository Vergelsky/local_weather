from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def index(request):
    context = {
        'title': "Местная погода"
    }

    return render(request, 'local_weather/index.html', context)

def get_weather(request):
    city = request.GET.get('city')
    data = {
        'weather': f"Погода в городе {city} сегодня очено хорошая"
    }
    return JsonResponse(data)