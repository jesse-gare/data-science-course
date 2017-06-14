import requests
url = "https://www.quandl.com/api/v3/datasets/EOD/KO.csv?api_key=P1yyj5xSCdFcEMkC7rj8"
response = requests.get(url)
print(response.text)
