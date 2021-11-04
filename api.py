from os import error
from re import match
from typing import Dict
import flask
from flask import jsonify, request
import json

with open("countries.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    
# keys definition

allkeys = ['id', 
        'name', 
        'iso3', 
        'iso2', 
        'numeric_code', 
        'phone_code', 
        'capital', 
        'currency', 
        'currency_symbol', 
        'tld', 
        'native', 
        'region', 
        'subregion', 
        'timezones', 
        'translations', 
        'latitude', 
        'longitude', 
        'emoji', 
        'emojiU']

timezonekeys = ['zoneName', 
                'gmtOffset', 
                'gmtOffsetName', 
                'abbreviation', 
                'tzName']

# end of keys definition


app = flask.Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return flask.render_template("simplepage.html")


@app.route("/api/countries/all", methods=["GET"])
def api_all():
    return jsonify(data)


@app.route("/api/countries/country", methods=["GET"])
def api_id():

    results = []

    # for key in allkeys:
    #     if key in request.args:
    #         for country in data:
    #             if str(country[key]) == request.args[key] and country not in results:
    #                 results.append(country)


    # for key in request.args:
    #     for country in data:
    #         try:
    #             if str(country[key]) == request.args[key] and country not in results:
    #                 results.append(country)
    #         except KeyError:
    #             return "We can't find all the keys"


    for country in data:

        print("******")
        match = True

        try:

            for key in request.args:
                print(f"{country[key]} = {request.args[key]} = {country[key] == request.args[key]}")
                match = match and (str(country[key]) == request.args[key])
                print(f"match == {match}")

            if match: results.append(country)

        except KeyError:
            return "We can't find all the keys"
        
    return jsonify(results)
    
    

@app.route("/api/settings", methods=["GET"])
def getType():

    print(type(data))
    return f"EHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\nEHHHHHHHHHHHHHHHHHHHHH"

app.run()
