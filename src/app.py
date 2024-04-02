from dotenv import load_dotenv
from flask import Flask, render_template
from flask_cors import CORS
import os
from src.views.GptView import chatGptApi


def createApp():
    load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
    app = Flask(__name__)

    # Cors Origin initialize
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Flask configuration initialize
    app.config.from_pyfile('config/configurations.py')

    # Register blueprints
    app.register_blueprint(chatGptApi, url_prefix="/api/v1")

    @app.route('/')
    def home():
        return render_template('index.html')

    return app
