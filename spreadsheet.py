import os
import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class SpreadSheet(object):
    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        credential = {
            "type": os.environ['GS_CREDENTIAL_TYPE'],
            "project_id": os.environ['GS_PROJECT_ID'],
            "private_key_id": os.environ['GS_PRIVATE_KEY_ID'],
            "private_key": os.environ['GS_PRIVATE_KEY'],
            "client_email": os.environ['GS_CLIENT_EMAIL'],
            "client_id": os.environ['GS_CLIENT_ID'],
            "auth_uri": os.environ['GS_AUTH_URI'],
            "token_uri": os.environ['GS_TOKEN_URI'],
            "auth_provider_x509_cert_url": os.environ['GS_AUTH_PROVIDER_CERT_URL'],
            "client_x509_cert_url":  os.environ['GS_CLIENT_CERT_URL']
        }
        cred = ServiceAccountCredentials.from_json_keyfile_dict(
            credential, scope)
        self.gs = gspread.authorize(cred)

    def open_sheet(self, filename):
        return self.gs.open(filename).sheet1
