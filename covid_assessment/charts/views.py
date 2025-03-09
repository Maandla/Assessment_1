from django.shortcuts import render
import json
from django.http import JsonResponse

def chart_view(request):
    with open('charts/static/charts/covid.json', 'r') as file:
        data = json.load(file)

    return render(request, 'charts/chart.html', {'covid_data': json.dumps(data)})

