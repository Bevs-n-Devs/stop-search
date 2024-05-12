import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)

if __name__ == "__main__":
    app.run(
        debug=True,
        port=os.environ["API_PORT"],
        host=os.environ["API_HOST"],
    )

from stopSearch.main import *
