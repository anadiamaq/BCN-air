from main import app
from flask import request
from utils.json_response import json_response
from mongo_connection import mongo_read
from utils.handle_error import handle_error

# To avoid errors due to the data type (str or int), a dictionary is created with a key with the names of the columns that will be query params and another with a function that transforms the result of the request into the desired data type.
@app.get("/read_air_qa")
@handle_error
def read_mongo_air():
    query_params = [
        {"name": "Station", "cast": str},
        {"name": "Air_Quality", "cast": str},
        {"name": "O3_Quality", "cast": str},
        {"name": "O3_Value", "cast": int},
        {"name": "NO2_Quality", "cast": str},
        {"name": "NO2_Value", "cast": int},
        {"name": "PM10_Quality", "cast": str},
        {"name": "PM10_Value", "cast": int},
        {"name": "Date", "cast": str},
    ]
    q = {
        query_param["name"]: query_param["cast"](request.args.get(query_param["name"]))
        for query_param in query_params
        if request.args.get(query_param["name"])
    }
    return json_response(list(mongo_read("Enviromental_Health_BCN", "Air_QA", q)))


@app.get("/read_deaths_2018")
@handle_error
def read_mongo_deaths():
    query_params = [
        {"name": "Districts", "cast": str},
        {"name": "Total_deaths", "cast": int},
        {"name": "Men", "cast": int},
        {"name": "Women", "cast": int},
    ]
    q = {
        query_param["name"]: query_param["cast"](request.args.get(query_param["name"]))
        for query_param in query_params
        if request.args.get(query_param["name"])
    }
    return json_response(list(mongo_read("Enviromental_Health_BCN", "Deaths_2018", q)))


@app.get("/read_air_stations")
@handle_error
def read_mongo_stations():
    query_params = [
        {"name": "Station", "cast": str},
        {"name": "Longitude", "cast": int},
        {"name": "Latitude", "cast": int},
        {"name": "Ubication", "cast": str},
        {"name": "District Name", "cast": str},
        {"name": "Neighborhood Name", "cast": str},
    ]
    q = {
        query_param["name"]: query_param["cast"](request.args.get(query_param["name"]))
        for query_param in query_params
        if request.args.get(query_param["name"])
    }
    return json_response(list(mongo_read("Enviromental_Health_BCN", "Air_stations", q)))
