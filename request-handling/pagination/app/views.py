from django.shortcuts import render_to_response, redirect
from django.urls import reverse

from csv import DictReader

from app.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    per_page = 10
    input_file = DictReader(open(BUS_STATION_CSV))
    stations = []
    for station in input_file:
        stations.append({'Name': station['Name'], 'Street': station['Street'], 'District': station['District']})

    number_of_page = int(request.GET.get('page')) or 1

    return render_to_response('index.html', context={
        'bus_stations': stations[number_of_page: number_of_page + per_page],
        'current_page': number_of_page,
        'prev_page_url': None if number_of_page == 1 else f'bus_stations?page={number_of_page - 1}',
        'next_page_url': f'bus_stations?page={number_of_page + 1}',
    })
