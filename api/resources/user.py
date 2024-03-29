from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from api.schemas import UserSchema, UserUpdateSchema
from db import db
from models import UserModel

user_blueprint = Blueprint('Users', 'users', description='User operations')


@user_blueprint.route('/users/', methods=['GET', 'POST'])
class UserList(MethodView):
    @user_blueprint.response(200, UserSchema(many=True))
    def get(self):
        """Get all users."""
        return UserModel.query.all()

    @user_blueprint.arguments(UserSchema)
    def post(self, user_data):
        """Create a new user."""
        if UserModel.query.filter_by(username=user_data['username']).first():
            abort(409, message='Username already exists')

        user = UserModel(full_name=user_data['full_name'], username=user_data['username'],
                         password=pbkdf2_sha256.hash(user_data['password']),
                         confirm_password=pbkdf2_sha256.hash(user_data['confirm_password']))
        db.session.add(user)
        db.session.commit()

        return {'message': 'User created successfully'}, 201


@user_blueprint.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
class UserDetail(MethodView):
    @user_blueprint.response(200, UserSchema)
    def get(self, user_id):
        """Get a user by ID."""
        user = UserModel.query.get_or_404(user_id, description='User not found')

        return user

    @user_blueprint.arguments(UserUpdateSchema)
    @user_blueprint.response(200, UserSchema)
    def put(self, user_data, user_id):
        """Update a user by ID."""
        user = UserModel.query.get_or_404(user_id)

        if user:
            user.full_name = user_data.get('full_name', user.full_name)
            user.username = user_data.get('username', user.username)
            user.password = user_data.get('password', user.password)
            user.confirm_password = user.password
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

    @user_blueprint.response(204, UserSchema)
    def delete(self, user_id):
        """Delete a user by ID."""
        user = UserModel.query.get_or_404(user_id, description='User not found')

        db.session.delete(user)
        db.session.commit()

        return {'message': 'User deleted'}
