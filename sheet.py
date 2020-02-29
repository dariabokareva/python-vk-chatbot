from typing import List, Any
import httplib2  # google-api-python-client
from httplib2 import ProxyInfo, socks
from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials  # oauth2client
import pandas as pd
from urllib.parse import urlparse
import os
import numpy as np

# from server import Server

CREDENTIALS_FILE = 'chatbot-vk-instagram-11994c762d7a.json'
SPREADSHEET_ID = '1ZC8ll2CE9KKEU8JdXm2nJmusivOlTiLLN3Hka9Y82S0'
RANGE_NAME = 'B4:F500'

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

key = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)

# proxy_netloc = urlparse(os.environ.get("http_proxy")).netloc.split(':')
'''httpAuth = key.authorize(httplib2.Http(proxy_info=ProxyInfo(proxy_type=socks.PROXY_TYPE_HTTP,
                                                            proxy_host=proxy_netloc[0],
                                                            proxy_port=int(proxy_netloc[1]))))'''
httpAuth = key.authorize(httplib2.Http())
print(httpAuth)
print(key)
service = discovery.build('sheets', 'v4', http=httpAuth)

sheet = service.spreadsheets()


def dataframe_to_list(df):
    Row_list: List[List[Any]] = []
    # Итерировать по каждой строке
    for i in range((df.shape[0])):
        # Использование iloc для доступа к значениям
        # текущая строка, обозначенная "i"
        Row_list.append(list(df.iloc[i, :]))
    return Row_list


df = pd.DataFrame(columns=['Date', 'Username', 'Link', 'Message', 'Other'])


def df_append(df, data):
    df = df.append({'Date': data[0], 'Username': data[1], 'Link': data[2], 'Message': data[3], 'Other': data[4]},
                   ignore_index=True)
    result = dataframe_to_list(df)
    return df, result


def sheet_append(sheet, values):
    sheet.values().clear(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME, body={}).execute()
    spreadsheet = sheet.values().append(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME, body={
        "majorDimension": "ROWS",
        "values": values},
                                        valueInputOption="USER_ENTERED").execute()

# spreadsheet2 = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
# values = spreadsheet2.get('values', [])
# print(values)
