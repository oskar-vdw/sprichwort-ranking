import requests
import json

url = 'http://127.0.0.1:5000/addsw'


headers = {
    'Content-Type': 'application/json'
}
with open('sprichwort_liste_neu.json', 'r') as file:
    sprichworter = json.load(file)
    
for i in sprichworter:
    print(i['sprichwort'])
    
    data = {
    'content': i['sprichwort'],
    'explanation': i['erklaerung'],
    'icon': i['icon'],
    'matchesplayed': 0,
    'elo': 1200,
    }
    print(data)
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        print(response.text)
    else:
        print("Success")



