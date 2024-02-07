import os

from flask import Flask
from flask_smorest import Api

from api.resources.user import user_blueprint
from db import db


def create_app():
    app = Flask(__name__)
    app.config['PROPAGATE_EXCEPTIONS'] = True  # Change to False in production
    app.config['API_TITLE'] = 'Stationery Shop API'
    app.config['API_VERSION'] = 'v1.0'
    app.config['OPENAPI_VERSION'] = '3.1.0'
    app.config['OPENAPI_URL_PREFIX'] = '/'
    app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'
    app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///stationery_shop.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # Change to False in production

    db.init_app(app)

    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(user_blueprint, url_prefix=f'/api/{app.config["API_VERSION"]}')

    return app
