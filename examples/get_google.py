import requests

response = requests.get("http://google.com")

with open("google.html", 'w') as out_file:
    out_file.write(response.text)
