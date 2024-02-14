from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256

from api.schemas.user import UserLoginSchema
from models import UserModel

auth_blueprint = Blueprint("Auth", "auth", description="Authentication operations")


@auth_blueprint.route('/login/', methods=['POST'])
class UserLogin(MethodView):
    @auth_blueprint.arguments(UserLoginSchema)
    def post(self, user_data):
        user = UserModel.query.filter(UserModel.username == user_data['username']).first()

        if user and pbkdf2_sha256.verify(user_data['password'], user.password):
            return {'message': 'Logged in successfully.'}, 200

        abort(401, message='Invalid username or password.')
