from flask import Flask
from .index import  main_routes




def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_routes)
    return app

