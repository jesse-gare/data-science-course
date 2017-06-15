#!/usr/bin/env python

import requests
import json
import re

API_KEY = 'mu88bd25bwe4e3z5d8b73byy'
AUTH= '/?apiKey=' + API_KEY
BASE_URL = "http://api.ft.com"

def search(terms):
    """
    Get the headline data by searching with the given terms.
    """

    path = "/content/search/v1"
    url = BASE_URL + path + AUTH

    query_string = " ".join(terms)
    data = {"queryString": query_string,
            "queryContext": { "curations" : ["ARTICLES"] } }

    response = requests.post(url, json=data)
    data = response.json()

    return data

def print_headlines(searched):
    """
    Get the first headline in the searched headlines data.
    """
    results = searched["results"][0]["results"]
    for index, result in enumerate(results):
        content_id = results[index]["id"]
        url =  "https://www.ft.com/content/" + content_id
        response = requests.get(url)
        data = response.text
        with open("out.html", 'w') as out_file:
            out_file.write(content_id)
            out_file.write(data)
        title_pattern = r'article-title(?:--redesign)?\">(.*?)<'
        headline = re.findall(title_pattern, data)
        if headline:
            print(headline[0]) 

if __name__ == "__main__":

    import sys

    try:
        terms = sys.argv[1:]
    except:
        print("Need to input some search terms.")

    searched = search(terms)
    print_headlines(searched)
