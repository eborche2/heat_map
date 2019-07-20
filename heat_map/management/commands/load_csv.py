from pathlib import Path

from django.conf import settings
from django.core.management import BaseCommand
from heat_map.models import Ipv

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
        count = df.groupby(df.columns.tolist(), as_index=False).size()
        ipv = None
        if 'IPv4' in file_name:
            ipv = 'ipv4'
        if 'IPv6' in file_name:
            ipv = 'ipv6'

        for index, row in count.iteritems():
            Ipv.objects.update_or_create(
                latitude=index[0],
                longitude=index[1],
                defaults= {
                    ipv: row
                }
            )
