import os
import secrets

from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager

from api.resources.user import user_blueprint
from api.resources.auth import auth_blueprint
from blocklist import BLOCKLIST
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

    app.config['JWT_SECRET_KEY'] = secrets.token_urlsafe(64)

    jwt = JWTManager(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload['jti'] in BLOCKLIST

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return jsonify({'message': 'The token has been revoked.', 'error': 'token_revoked'}), 401

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({'message': 'The token has expired.', 'error': 'token_expired'}), 401

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({'message': 'Signature verification failed.', 'error': 'invalid_token'}), 401

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({'message': 'Request does not contain an access token.', 'error': 'authorization_required'}), 401

    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return jsonify({'message': 'The token is not fresh.', 'error': 'fresh_token_required'}), 401

    db.init_app(app)

    api = Api(app)

    with app.app_context():
        db.create_all()

    base_url_prefix = f'/api/{app.config["API_VERSION"]}'
    api.register_blueprint(user_blueprint, url_prefix=f'{base_url_prefix}')
    api.register_blueprint(auth_blueprint, url_prefix=f'{base_url_prefix}/auth')

    return app
