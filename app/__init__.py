from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()  

def create_app():
    myapp_obj = Flask(__name__)  
    basedir = os.path.abspath(os.path.dirname(__file__))

    myapp_obj.config.from_mapping(
        SECRET_KEY='you-will-never-guess',
        SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'app.db'),
    )

    db.init_app(myapp_obj)  

    
    with myapp_obj.app_context():
        from app import routes, models

    return myapp_obj
