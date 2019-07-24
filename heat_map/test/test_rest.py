import json

from django.conf.global_settings import DEFAULT_CHARSET
from rest_framework.test import APITestCase

from heat_map.models import Ipv


class RestTestCase(APITestCase):
    def setUp(self):
        Ipv.objects.create(
            latitude=34.000,
            longitude=80.000,
            ipv4=4,
            ipv6=0
        )
        Ipv.objects.create(
            latitude=-45.000,
            longitude=-150.000,
            ipv4=6
        )
        Ipv.objects.create(
            latitude=00.00,
            longitude=00.00,
            ipv4=0,
            ipv6=0
        )
        self.json_data_first = [
            {"id": 1, "latitude": "34.000000", "longitude": "80.000000", "ipv4": 4, "ipv6": 0, "level": 1}]
        self.json_data_second = [
            {'id': 2, 'latitude': '-45.000000', 'longitude': '-150.000000', 'ipv4': 6, 'ipv6': 0, 'level': 1}]
        self.json_data_third = [
            {'id': 3, 'latitude': '0.000000', 'longitude': '0.000000', 'ipv4': 0, 'ipv6': 0, 'level': 1}]

    def test_rest_results_success(self):
        rsp = self.client.get(
            '/api/ipv?upper_lat=37.326488613342086&lower_lat=33.31168124115256&lower_long=79.54577636718751&upper_long=81.24536132812501')
        self.assertEqual(200, rsp.status_code)
        self.assertEqual(self.json_data_first, json.loads(rsp.content.decode(DEFAULT_CHARSET)))
        rsp = self.client.get(
            '/api/ipv?upper_lat=-45&lower_lat=-45&lower_long=-150&upper_long=-150')
        self.assertEqual(200, rsp.status_code)
        self.assertEqual(self.json_data_second, json.loads(rsp.content.decode(DEFAULT_CHARSET)))
        rsp = self.client.get(
            '/api/ipv?upper_lat=0&lower_lat=0&lower_long=0&upper_long=0')
        self.assertEqual(200, rsp.status_code)
        self.assertEqual(self.json_data_third, json.loads(rsp.content.decode(DEFAULT_CHARSET)))

    def test_rest_results_none(self):
        rsp = self.client.get(
            '/api/ipv?upper_lat=34.01&lower_lat=34.02&lower_long=80.01&upper_long=80.02')
        self.assertEqual(200, rsp.status_code)
        self.assertEqual([], json.loads(rsp.content.decode(DEFAULT_CHARSET)))
        rsp = self.client.get(
            '/api/ipv?upper_lat=33&lower_lat=34&lower_long=79&upper_long=80')
        self.assertEqual(200, rsp.status_code)
        self.assertEqual([], json.loads(rsp.content.decode(DEFAULT_CHARSET)))

    def test_rest_missing_query(self):
        rsp = self.client.get('/api/ipv?upper_lat=34.01&lower_lat=34.02')
        self.assertEqual(200, rsp.status_code)
        self.assertEqual([], json.loads(rsp.content.decode(DEFAULT_CHARSET)))

    def test_rest_get_no_query(self):
        rsp = self.client.get('/api/ipv')
        self.assertEqual(200, rsp.status_code)
        self.assertEqual([], json.loads(rsp.content.decode(DEFAULT_CHARSET)))

