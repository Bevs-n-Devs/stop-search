import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Set configuration variables
app.config['USER_AGENT'] = 'stopSearchApp/1.0'
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'templates', 'static', 'assets')
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024 * 1024  # Max file size: 2GB

if __name__ == "__main__":
    app.run(
        debug=True,
        port=os.environ["API_PORT"],
        host=os.environ["API_HOST"],
    )

from stopSearch.main import *
