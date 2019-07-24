import csv
import os
from pathlib import Path

from django.conf import settings
from django.core.management import call_command
from django.test import TestCase
from heat_map.models import Ipv

class TestLoadCSV(TestCase):
    def setUp(self):
        with open(Path(settings.BASE_DIR, 'testIPv4.csv'), 'w') as testFile:
            fieldnames = ['network', 'geoname_id', 'registered_country_geoname_id', 'represented_country_geoname_id',
                          'is_anonymous_proxy', 'is_satellite_provider', 'postal_code', 'latitude', 'longitude',
                          'accuracy_radius']
            writer = csv.writer(testFile)
            writer.writerow(fieldnames)
            writer.writerow(
                ['1.0.0.0/24', 2067951, 2077456, '', 0, 0, 5255, -35.3010, 139.0453, 50])
            writer.writerow(
                ['1.0.0.0/24', 2067951, 2077456, '', 0, 0, 5255, -35.3010, 139.0453, 50])
            writer.writerow(
                ['1.0.0.0/24', 2067951, 2077456, '', 0, 0, 5255, 26, 118, 50])
            writer.writerow(
                ['1.0.0.0/24', 2067951, 2077456, '', 0, 0, 5255, 26, 118, 50])
        with open(Path(settings.BASE_DIR, 'testIPv6.csv'), 'w') as testFile:

            writer = csv.writer(testFile)
            writer.writerow(fieldnames)
            writer.writerow(
                ['1.0.0.0/24', 2067951, 2077456, '', 0, 0, 5255, -50, 80, 50])
            writer.writerow(
                ['1.0.0.0/24', 2067951, 2077456, '', 0, 0, 5255, 0, 0, 50])
            writer.writerow(
                ['1.0.0.0/24', 2067951, 2077456, '', 0, 0, 5255, 26, 118, 50])
            writer.writerow(
                ['1.0.0.0/24', 2067951, 2077456, '', 0, 0, 5255, 26, 118, 50])

    def test_csv_load(self):
        args = []
        opts = {'filename': 'testIPv4.csv'}
        call_command('load_csv', *args, **opts)
        self.assertTrue(Ipv.objects.filter(latitude=26, longitude=118, ipv4=2, ipv6=0).exists())
        self.assertTrue(Ipv.objects.filter(latitude=-35.3010, longitude=139.0453, ipv4=2, ipv6=0).exists())
        opts = {'filename': 'testIPv6.csv'}
        call_command('load_csv', *args, **opts)
        self.assertTrue(Ipv.objects.filter(latitude=26, longitude=118, ipv4=2, ipv6=2).exists())
        self.assertTrue(Ipv.objects.filter(latitude=-35.3010, longitude=139.0453, ipv4=2, ipv6=0).exists())
        self.assertTrue(Ipv.objects.filter(latitude=0, longitude=0, ipv4=0, ipv6=1).exists())
        self.assertTrue(Ipv.objects.filter(latitude=-50, longitude=80, ipv4=0, ipv6=1).exists())
        self.assertEqual(4, len(Ipv.objects.all()))

    def tearDown(self):
        os.remove(Path(settings.BASE_DIR, 'testIPv4.csv'))
        os.remove(Path(settings.BASE_DIR, 'testIPv6.csv'))
