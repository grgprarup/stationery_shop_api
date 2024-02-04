from flask.views import MethodView
from flask_smorest import Blueprint

from api.schemas.user import UserSchema
from api.models.user import User
from db import db


class UserService:
    user_schema = UserSchema()

    @staticmethod
    def get_all_users():
        """Get all users"""
        users = User.query.all()
        return UserService.user_schema.dump(users, many=True)

    @staticmethod
    def create_user(user_data):
        """Create a new user."""
        result, errors = UserService.user_schema.load(user_data)

        if errors:
            return False, errors

        if User.query.filter_by(username=result['username']).first():
            return False, 'Username already exists'

        new_user = User(username=result['username'], password=result['password'])
        db.session.add(new_user)
        db.session.commit()

        return True, 'User created successfully'

    @staticmethod
    def get_user(user_id):
        pass

    @staticmethod
    def update_user(user_id, data):
        pass

    @staticmethod
    def delete_user(user_id):
        pass
