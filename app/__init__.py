from flask import Flask
from flask import session
from pymongo import MongoClient
import os

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'task_manager_secret_key')

    # Database
    client = MongoClient('mongodb+srv://devanshu:cXGqHvLx6kxIebHR@cluster0.tpjj51d.mongodb.net/')
    db = client.task_manager

    from .routes import main
    main.db = db

    app.register_blueprint(main)

    return app
