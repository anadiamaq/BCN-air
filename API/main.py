from flask import Flask

app = Flask("BCN_air-api")


@app.route("/")
def title():
    return '<h1 align="center">Air quality in BCN</h1>'

