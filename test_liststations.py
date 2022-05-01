# Author Sravanaswathi Sajja
# Version 1.0
#file name:test_liststations.py

import json

import requests


def test_api():
    # get request to virta api
    response = requests.get("https://api.virta.fi/v4/stations?latMin=60.1652&latMax=60.1653&longMin=24&longMax=25")
    # getting response as json object
    json_response = response.json()

    # dump the JSON object to string
    js = json.dumps(json_response)
    print("JSON String Output \n", js)

    # load the JSON string into dictionary / Parse the json object
    js1 = json.loads(js)
    print("JSON Dictionary Output \n",js1)

    # print the JSON dictionary response
    print("Virta Response \n", js1[0])

    # validate the json object using specific id from the response
    assert json_response[0]["id"] == 21027," ID not found"
    print("Virta API Response \n", json_response[0])

# JSON object - JSON String - Parsing - JSON Object


