from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.core.paginator import Paginator

from csv import DictReader

from django.conf import settings


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    read_file_with_station = list(DictReader(open(settings.BUS_STATION_CSV, encoding='cp1251')))

    paginator = Paginator(read_file_with_station, 10)
    current_page = int(request.GET.get('page', 1))
    current_stations = paginator.page(current_page)

    return render_to_response('index.html', context={
        'bus_stations': current_stations.object_list,
        'current_page': current_page,
        'prev_page_url': f'bus_stations?page={current_stations.previous_page_number()}'
        if current_stations.has_previous() else None,
        'next_page_url': f'bus_stations?page={current_stations.next_page_number()}'
        if current_stations.has_next() else None,
    })
