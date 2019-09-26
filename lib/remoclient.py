import os
import requests
import json


class NatureRemoClient(object):
    def __init__(self, base_url=None):
        if base_url:
            self.base_url = base_url
        else:
            self.base_url = 'https://api.nature.global'
        token = os.environ.get('REMO_TOKEN')
        if token:
            raise Exception('Please set your API token to REMO_TOKEN')
        self.headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer ' + token
        }

    def call_api(self, url, method='get', params=None):
        req_method = getattr(requests, method)
        try:
            res = req_method(self.base_url+url,
                             headers=self.headers,
                             params=params)
            return res.json()
        except Exception as e:
            raise Exception('Failed to call API: %s' % str(e))

    def get_devices(self):
        url = '/1/devices'
        return self.call_api(url)

    def get_device(self, device_name=None, device_id=None):
        devices = self.get_devices()
        if device_id:
            device = [d for d in devices if d['id'] == device_id]
            return device[0]
        elif device_name:
            device = [d for d in devices if d['name'] == device_name]
            return device[0]
        else:
            return devices[0]

    def get_newest_events(self, device_name=None, device_id=None,
                          event_name=None):
        if device_name:
            device = self.get_device(device_name=device_name)
        elif device_id:
            device = self.get_device(device_id=device_id)
        else:
            device = self.get_device()
        if event_name:
            return device['newest_events'][event_name]
        else:
            return device['newest_events']

    def get_temperature(self, device_name=None, device_id=None):
        return self.get_newest_events(device_name=device_name,
                                      device_id=device_id, event_name='te')

    def get_humidity(self, device_name=None, device_id=None):
        return self.get_newest_events(device_name=device_name,
                                      device_id=device_id, event_name='hu')

    def get_illumination(self, device_name=None, device_id=None):
        return self.get_newest_events(device_name=device_name,
                                      device_id=device_id, event_name='il')

    def get_motion(self, device_name=None, device_id=None):
        return self.get_newest_events(device_name=device_name,
                                      device_id=device_id, event_name='mo')
