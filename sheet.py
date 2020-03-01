from typing import List, Any
import httplib2  # google-api-python-client
from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials  # oauth2client
import pandas as pd
import numpy as np

# from server import Server

CREDENTIALS_FILE = 'your-google-credentials-file.json'
SPREADSHEET_ID = 'your google shet id'
RANGE_NAME = 'cell range (ex. A1:E5)'

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

key = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)

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
