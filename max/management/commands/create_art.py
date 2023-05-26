from django.core.management.base import BaseCommand
from max.models import Edition
import json
from pprint import pprint


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('num', type=int)
       


    def handle(self, *args, **options):
        print(options['num'])

        with open('data_items.json','r', encoding='utf8')as file:
            file = file.read()
            json_data =  json.loads(file)

            for art in json_data:
                Edition.objects.create(
                    name=art['Название'],
                    slug=art['Название'].lower(),
                    description=art['Контент'],
                )
        