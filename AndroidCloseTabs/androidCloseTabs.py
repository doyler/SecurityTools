import json
import requests

response = requests.get("http://localhost:9222/json/list")

#print(response.text.encode('utf-8'))

json_data = json.loads(response.text.encode('utf-8'))

for link in json_data:
    #print(link['id'])
    response = requests.get("http://localhost:9222/json/close/" + link['id'])
    print(response.text)