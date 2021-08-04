from flask import Flask
import json
import os

app = Flask('BCN_air')

PORT = os.getenv('PORT')

app.run('0.0.0.0', PORT, debug=True)

def
