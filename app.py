from flask import Flask
from flask_smorest import Api

from api.routes.user_routes import user_routes
from db import db

app = Flask(__name__)
app.config['API_TITLE'] = 'Stationery Shop API'
app.config['API_VERSION'] = 'v1.0'
app.config['OPENAPI_VERSION'] = '3.0.3'
app.config['OPENAPI_URL_PREFIX'] = '/'
app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'
app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stationery_shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

api = Api(app)

with app.app_context():
    db.create_all()

api.register_blueprint(user_routes, url_prefix='/api/v1.0')

if __name__ == '__main__':
    app.run(debug=True)
