from flask import Flask, jsonify


app = Flask('HelloWorldApp')


@app.route("/")
def hello_world():
    return jsonify(hello="world")