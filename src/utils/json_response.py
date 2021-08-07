from flask import Response
from bson.json_util import dumps
from json import loads


def json_response(data, status=200):
    return Response(
        dumps(data),
        status,
        mimetype='application/json')

def str_to_json(data):
    return loads(data)
