import os
import pathlib
import sys
import unittest
import requests
from unittest.mock import patch

import lib.remoclient as remoclient
import tests.constants as constants


def requests_get_mock(*args, **kwargs):
    class ResponseMock:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == constants.REMO_DEVICES_URL:
        return ResponseMock(constants.REMO_DEVICES, 200)
    else:
        return ResponseMock(None, 404)


class RemoclientTest(unittest.TestCase):

    def setUp(self):
        os.environ['REMO_TOKEN'] = 'test'

    @patch('requests.get', side_effect=requests_get_mock)
    def test_get_device(self, mock_func):
        client = remoclient.NatureRemoClient()
        res = client.get_device()

        self.assertEqual(res['name'], constants.REMO_DEVICES[0]['name'])

    @patch('requests.get', side_effect=requests_get_mock)
    def test_get_device_by_name(self, mock_func):
        client = remoclient.NatureRemoClient()
        res = client.get_device(device_name=constants.REMO_DEVICES[0]['name'])

        self.assertEqual(res['name'], constants.REMO_DEVICES[0]['name'])

    @patch('requests.get', side_effect=requests_get_mock)
    def test_get_device_by_id(self, mock_func):
        client = remoclient.NatureRemoClient()
        res = client.get_device(device_id=constants.REMO_DEVICES[1]['id'])

        self.assertEqual(res['name'], constants.REMO_DEVICES[1]['name'])

    @patch('requests.get', side_effect=requests_get_mock)
    def test_get_newest_events(self, mock_func):
        client = remoclient.NatureRemoClient()
        res = client.get_newest_events()

        self.assertEqual(res, constants.REMO_DEVICES[0]['newest_events'])

    @patch('requests.get', side_effect=requests_get_mock)
    def test_get_newest_events_by_device_name(self, mock_func):
        client = remoclient.NatureRemoClient()
        res = client.get_newest_events(
            device_name=constants.REMO_DEVICES[0]['name'])

        self.assertEqual(res, constants.REMO_DEVICES[0]['newest_events'])

    @patch('requests.get', side_effect=requests_get_mock)
    def test_get_newest_events_by_device_id(self, mock_func):
        client = remoclient.NatureRemoClient()
        res = client.get_newest_events(
            device_id=constants.REMO_DEVICES[0]['id'])

        self.assertEqual(res, constants.REMO_DEVICES[0]['newest_events'])

    @patch('requests.get', side_effect=requests_get_mock)
    def test_get_temperature(self, mock_func):
        client = remoclient.NatureRemoClient()
        res = client.get_temperature()

        self.assertEqual(res, constants.REMO_DEVICES[0]['newest_events']['te'])

    @patch('requests.get', side_effect=requests_get_mock)
    def test_get_temperature_by_device_name(self, mock_func):
        client = remoclient.NatureRemoClient()
        res = client.get_temperature(
            device_name=constants.REMO_DEVICES[0]['name'])

        self.assertEqual(res, constants.REMO_DEVICES[0]['newest_events']['te'])

    @patch('requests.get', side_effect=requests_get_mock)
    def test_get_temperature_by_device_id(self, mock_func):
        client = remoclient.NatureRemoClient()
        res = client.get_temperature(
            device_id=constants.REMO_DEVICES[0]['id'])

        self.assertEqual(res, constants.REMO_DEVICES[0]['newest_events']['te'])

    @patch('requests.get', side_effect=requests_get_mock)
    def test_get_humidity(self, mock_func):
        client = remoclient.NatureRemoClient()
        res = client.get_humidity()

        self.assertEqual(res, constants.REMO_DEVICES[0]['newest_events']['hu'])

    @patch('requests.get', side_effect=requests_get_mock)
    def test_get_humidity_by_device_name(self, mock_func):
        client = remoclient.NatureRemoClient()
        res = client.get_humidity(
            device_name=constants.REMO_DEVICES[0]['name'])

        self.assertEqual(res, constants.REMO_DEVICES[0]['newest_events']['hu'])

    @patch('requests.get', side_effect=requests_get_mock)
    def test_get_humidity_by_device_id(self, mock_func):
        client = remoclient.NatureRemoClient()
        res = client.get_humidity(
            device_id=constants.REMO_DEVICES[0]['id'])

        self.assertEqual(res, constants.REMO_DEVICES[0]['newest_events']['hu'])

    @patch('requests.get', side_effect=requests_get_mock)
    def test_get_illumination(self, mock_func):
        client = remoclient.NatureRemoClient()
        res = client.get_illumination()

        self.assertEqual(res, constants.REMO_DEVICES[0]['newest_events']['il'])

    @patch('requests.get', side_effect=requests_get_mock)
    def test_get_illumination_by_device_name(self, mock_func):
        client = remoclient.NatureRemoClient()
        res = client.get_illumination(
            device_name=constants.REMO_DEVICES[0]['name'])

        self.assertEqual(res, constants.REMO_DEVICES[0]['newest_events']['il'])

    @patch('requests.get', side_effect=requests_get_mock)
    def test_get_illumination_by_device_id(self, mock_func):
        client = remoclient.NatureRemoClient()
        res = client.get_illumination(
            device_id=constants.REMO_DEVICES[0]['id'])

        self.assertEqual(res, constants.REMO_DEVICES[0]['newest_events']['il'])

    @patch('requests.get', side_effect=requests_get_mock)
    def test_get_motion(self, mock_func):
        client = remoclient.NatureRemoClient()
        res = client.get_motion()

        self.assertEqual(res, constants.REMO_DEVICES[0]['newest_events']['mo'])

    @patch('requests.get', side_effect=requests_get_mock)
    def test_get_motion_by_device_name(self, mock_func):
        client = remoclient.NatureRemoClient()
        res = client.get_motion(
            device_name=constants.REMO_DEVICES[0]['name'])

        self.assertEqual(res, constants.REMO_DEVICES[0]['newest_events']['mo'])

    @patch('requests.get', side_effect=requests_get_mock)
    def test_get_motion_by_device_id(self, mock_func):
        client = remoclient.NatureRemoClient()
        res = client.get_motion(
            device_id=constants.REMO_DEVICES[0]['id'])

        self.assertEqual(res, constants.REMO_DEVICES[0]['newest_events']['mo'])
