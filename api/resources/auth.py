from flask.views import MethodView
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt, jwt_required, get_jwt_identity
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256

from api.schemas import UserLoginSchema
from blocklist import BLOCKLIST
from models import UserModel

auth_blueprint = Blueprint("Auth", "auth", description="Authentication operations")


@auth_blueprint.route('/login/', methods=['POST'])
class UserLogin(MethodView):
    @auth_blueprint.arguments(UserLoginSchema)
    def post(self, user_data):
        user = UserModel.query.filter(UserModel.username == user_data['username']).first()

        if user and pbkdf2_sha256.verify(user_data['password'], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {'access_token': access_token, 'refresh_token': refresh_token}, 200

        abort(401, message='Invalid username or password.')


@auth_blueprint.route('/logout/', methods=['DELETE'])
class UserLogout(MethodView):
    @jwt_required()
    def delete(self):
        jti = get_jwt()['jti']
        BLOCKLIST.add(jti)
        return {'message': 'Logged out successfully.'}, 200


@auth_blueprint.route('/refresh/', methods=['POST'])
class TokenRefresh(MethodView):
    @jwt_required(fresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user, fresh=False)

        jti = get_jwt()['jti']
        BLOCKLIST.add(jti)

        return {'access_token': new_access_token}, 200
