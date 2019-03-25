from django.shortcuts import render
from django.views.generic import TemplateView

import csv


def process(value):
    try:
        return float(value)
    except ValueError:
        return '-'


class InflationView(TemplateView):
    template_name = 'inflation.html'

    def get(self, request, *args, **kwargs):
        with open('inflation_russia.csv', encoding='utf-8', newline='') as inflation_file:
            inflation_data = list(csv.reader(inflation_file, delimiter=';'))
            names_column = inflation_data.pop(0)

        inflation_data = [list(map(process, data_of_year)) for data_of_year in inflation_data]
        context = {
            'first_column': names_column,
            'inflation_date': inflation_data
        }

        return render(request, template_name=self.template_name,
                      context=context)
