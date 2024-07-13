from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/hello", methods=['GET'])
def greeting_message():
    return "Hello, Welcome to my Python-Flask App for DuploCloud"