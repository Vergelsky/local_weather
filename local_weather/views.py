from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': "Местная погода"
    }

    return render(request, 'local_weather/index.html', context)
