from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint

from api.models.user import UserModel
from api.schemas.user import UserSchema
from api.services.user import UserService

user_blueprint = Blueprint('Users', 'users', description='User operations')


@user_blueprint.route('/users')
class Users(MethodView):
    @user_blueprint.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()


class User(MethodView):
    # @user_blueprint.route('/users')
    # @user_blueprint.response(200, UserSchema(many=True))
    # def get(self):
    #     users = UserModel.query.all()
    #     return users

    @user_blueprint.route('/users/<int:user_id>')
    @user_blueprint.response(200, UserSchema)
    def get(self, user_id):
        user = UserService.get_user_by_id(user_id)
        if user:
            return jsonify({'user': user})
        else:
            return jsonify({'message': 'User not found'}), 404


@user_blueprint.route('/register')
class UserRegister(MethodView):
    @user_blueprint.arguments(UserSchema)
    def post(self, user_data):
        print(user_data)
        message, status_code = UserService.create_user(user_data)

        return {'message': message}, status_code
