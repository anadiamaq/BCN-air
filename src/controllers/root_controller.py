from utils.json_response import json_response
from app import app
from flask import request
from utils.handle_error import handle_error


@app.route('/')
@handle_error
def ejemplo():
    alumno = {
        'name': 'pepe'
    }
    return json_response(alumno)


@app.route('/saludo')
@handle_error
def saludo_fn():
    print(request.args)
    name = request.args.get('name')
    surname = request.args.get('surname')
    #raise ValueError('MEC')
    return{
        'name': name,
        'surname': surname
    }
