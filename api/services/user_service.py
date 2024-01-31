from flask.views import MethodView
from flask_smorest import Blueprint

from schemas import UserSchema
from api.models.user import UserModel
from db import db

blueprint = Blueprint('Users', 'users', description='Operations on users')


@blueprint.route('/user')
class User(MethodView):
    @blueprint.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()
