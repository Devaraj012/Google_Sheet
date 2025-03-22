import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

auth=os.getenv('TOKEN')

url = "https://greenestep.giftai.co.in/api/v1/csv"

headers = {
  'Cookie': 'ticket=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InNoYXJlX2RldnJhal9pYnRAZ3JlZW5lc3RlcC5jb20iLCJpZCI6MTgsInR5cGUiOiJBRE1JTiIsImlhdCI6MTc0MjQ1ODk1NCwiZXhwIjoxNzQyNTAyMTU0fQ.M7vyPWohkSlKUao2vkaYD5RQtz7WbxyYpEw1Ge1YBF8',
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {auth}'
}
Collections=[
  {
  "collection_description": "Googlesheet",
  "collection_name": "JA Interactions by Stage",
  "collection_permission": "READ",
  "collection_type": "PUBLIC"
  }]

for collection in Collections:
  payload = json.dumps(collection)
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)