from flask import Flask, jsonify

app = Flask('HelloWorldApp')

@app.route("/hello")
def hello_world():
    return jsonify(hello="world")