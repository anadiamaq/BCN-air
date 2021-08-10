from main import app
from flask import request
from utils.json_response import json_response, str_to_json
from mongo_connection import mongo_read
from utils.json_response import str_to_json

@app.get('/read_air_qa')
def read_mongo_air():
    q = dict(request.args)
    if 'mongo_query' in q.keys():
        q=str_to_json(q['mongo_query'])
    return json_response(list(mongo_read('Enviromental_Health_BCN','Air_QA',q)))

@app.get('/read_deaths_2018')
def read_mongo_deaths():
    q = dict(request.args)
    if 'mongo_query' in q.keys():
        q=str_to_json(q['mongo_query'])
    return json_response(list(mongo_read('Enviromental_Health_BCN','Deaths_2018',q)))
