from pathlib import Path

from django.conf import settings
from django.core.management import BaseCommand
from heat_map.models import IpvFour, IpvSix

import pandas as pd

class Command(BaseCommand):

    @classmethod
    def add_arguments(cls, parser):
        parser.add_argument('filename', help='Name of csv to ingest', type=str, nargs='?', default=None)

    @classmethod
    def handle(cls, *_args, **options):
        file_name = options['filename']
        file_location = Path(settings.BASE_DIR, file_name)
        df = pd.read_csv(file_location, usecols=[7, 8])
        df = df.drop([0])
        ipv = None
        lats_and_longs = []
        if 'IPv4' in file_name:
            ipv = IpvFour
        if 'IPv6' in file_name:
            ipv = IpvSix

        for index, row in df.iterrows():
            lats_and_longs.append(ipv(latitude=row[0], longitude=row[1]))
        ipv.objects.all().delete()
        ipv.objects.bulk_create(lats_and_longs)
