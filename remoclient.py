import os
import requests
import json
# import logging

# logging.basicConfig(level=logging.DEBUG)

class NatureRemoClient(object):
    def __init__(self, base_url=None):
        if base_url:
            self.base_url = base_url
        else:
            self.base_url = 'https://api.nature.global'
        self.token = os.environ.get('REMO_TOKEN')
        if not self.token:
            print('Please set your API token to REMO_TOKEN')
            raise
        self.headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer ' + self.token
        }

    def call_api(self, url, method='get', params=None):
        req_method = getattr(requests, method)
        res = req_method(self.base_url+url,
                         headers=self.headers,
                         params=params)
        return res.json()

    def get_devices(self):
        url = '/1/devices'
        return self.call_api(url)
