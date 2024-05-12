from flask import Flask, jsonify
from stopSearch import app
from stopSearch.stopSearch_database.extension import init_db
init_db()

@app.route("/")
def index_route() -> list[dict]:
    hello = "hello world"
    return jsonify({'temp': hello})