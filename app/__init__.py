from flask import Flask
import os
from config.settings import Config
from app.database import init_db
from app.routes import register_routes

def create_app():
    #app = Flask(__name__, template_folder="templates") 
    app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))

    app.config.from_object(Config)

    # Initialize database
    init_db(app)

    # Register routes
    register_routes(app)

    return app
