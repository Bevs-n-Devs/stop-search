from flask import Flask, jsonify
from stopSearch import app
from random import randint

@app.route("/")
def index_route() -> list[dict]:
    hello = "hello world"
    return jsonify({'temp': hello})