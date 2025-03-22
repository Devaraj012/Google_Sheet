import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from datetime import datetime

scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    r"C:\Users\devar\Documents\Code\Message\SMS\credentials.json",
    scopes=scope
)
client = gspread.authorize(creds)

try:
    print("Available Spreadsheets:")
    spreadsheets = client.openall()
    for sheet in spreadsheets:
        print(f"- {sheet.title}")

    sheet = client.open("InteractionCounts")
    worksheet = sheet.get_worksheet(0)
    print("-------------------------------\n")

    data = worksheet.get_all_records()
    df = pd.DataFrame(data)
    name='JA Interactions.csv'
    df['Month']=pd.to_datetime(df['Month']).dt.strftime('%m-%d-%Y')
    df.to_csv(name,index=False)

except gspread.exceptions.SpreadsheetNotFound:
    print("Error: Spreadsheet not found. Ensure the following:")
    print("1. The spreadsheet name is correct.")
    print("2. The service account has access to the spreadsheet.")
    print("3. The spreadsheet is a Google Sheet and is shared correctly.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
    
#Upload to GIFT

import requests

url = "https://greenestep.giftai.co.in/api/v1/csv/upload?d_type=none&"

payload = {'collection_id': '237',
'type': 'Replace',
'fieldMapped': 'Object'}

files=[
  ('csvFile',('JA_Interactions.csv',open(r'C:\Users\devar\Documents\Code\Google_sheet\GES\JA Interactions.csv','rb'),'text/csv'))
]

headers = {
  'Cookie': 'ticket=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InNoYXJlX2RldnJhal9pYnRAZ3JlZW5lc3RlcC5jb20iLCJpZCI6MTgsInR5cGUiOiJBRE1JTiIsImlhdCI6MTc0MjQ1ODk1NCwiZXhwIjoxNzQyNTAyMTU0fQ.M7vyPWohkSlKUao2vkaYD5RQtz7WbxyYpEw1Ge1YBF8'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)    