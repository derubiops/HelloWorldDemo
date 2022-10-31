from flask import Flask, jsonify

app = Flask('HelloWorldDemo')

@app.route("/hello")
def hello_world():
    return jsonify(hello="world")