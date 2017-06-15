import requests
import json

url = "https://www.quandl.com/api/v3/datasets/EOD/KO.json?api_key=P1yyj5xSCdFcEMkC7rj8"

response = requests.get(url)

#with open("KO.json", 'w') as out_file:
#    out_file.write(response.text)

data = json.loads(response.text)
print(data)
