from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('Hello world')

    data_dict = {'name': 'Cristina', 'years': 37, 'cities': ['napoli', 'Melbourne', 'Lisboa']}

    return render(request, 'route_app_3/index.html', {'data': data_dict})

def detail(request, city):
    return HttpResponse( f"Benvenuta a {city}.")
