from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from db import db
from models.user import UserModel
from api.schemas.user import UserSchema, UserUpdateSchema

user_blueprint = Blueprint('Users', 'users', description='User operations')


class UserList(MethodView):
    """Get all users."""
    @user_blueprint.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()

    @user_blueprint.arguments(UserSchema)
    def post(self, user_data):
        """Create a new user."""
        if UserModel.query.filter_by(UserModel.username == user_data['username']).first():
            abort(409, message='Username already exists')

        user = UserModel(username=user_data['username'], password=pbkdf2_sha256.hash(user_data['password']))
        db.session.add(user)
        db.session.commit()

        return {'message': 'User created successfully'}, 201


class UserDetail(MethodView):
    """Get a user by ID."""
    @user_blueprint.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)

        return user

    @user_blueprint.arguments(UserUpdateSchema)
    @user_blueprint.response(200, UserSchema)
    def put(self, user_id, user_data):
        user = UserModel.query.get_or_404(user_id)

        if user:
            user.username = user_data.get('username', user.username)
            user.password = user_data.get('password', user.password)
        else:
            user = UserModel(id=user_id, **user_data)

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(409, message='User already exists')
        except SQLAlchemyError:
            abort(500, message='Error while updating the user')

        return user

    @user_blueprint.response(204)
    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()

        return {'message': 'User deleted'}
