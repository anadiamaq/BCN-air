from app import app
from flask import request
from utils.handle_error import handle_error


@app.route('/two')
@handle_error
def two_fn():
    return{
        'name': 'EMOJI'
    }
