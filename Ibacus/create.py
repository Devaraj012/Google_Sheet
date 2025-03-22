import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

auth=os.getenv('TOKEN')

url = "https://greenestep.giftai.co.in/api/v1/csv"

headers = {
  'Cookie': 'ticket=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImRldmFyYWpAaWJhY3VzdGVjaGxhYnMuaW4iLCJpZCI6NCwidHlwZSI6IkFETUlOIiwiaWF0IjoxNzQyNDU3OTM4LCJleHAiOjE3NDI1MDExMzh9.ndQq-fey7ovy9OOEfnXCraL5KsxK96fyPTtiziGVoB4',
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