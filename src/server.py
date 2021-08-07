from app import app
from config import PORT
from controllers.fetch import *

app.run('0.0.0.0', PORT, debug=True)
