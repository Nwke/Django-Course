import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from phones.models import Phone

ID = 0
NAME = 1
IMAGE = 2
PRICE = 3
DATE = 4
LTE = 5


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:
            phone_reader = csv.reader(csvfile, delimiter=';')
            next(phone_reader)  # skip header

            for line in phone_reader:
                date_object = datetime.strptime(line[DATE], '%Y-%m-%d')
                phone = Phone(id=int(line[ID]),
                              name=line[NAME],
                              image=line[IMAGE],
                              price=int(line[PRICE]),
                              release_date=date_object,
                              lte_exists=line[LTE],
                              slug=slugify(line[NAME]))
                phone.save()
