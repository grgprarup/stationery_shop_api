from flask.views import MethodView
from flask_smorest import Blueprint

from api.schemas.user_schema import UserSchema
from api.models.user_model import UserModel
from db import db


class UserService:
    user_schema = UserSchema()
    @staticmethod
    def get_all_users():
        """Get all users"""
        users = UserModel.query.all()
        return UserService.user_schema.dump(users, many=True)

    @staticmethod
    def create_user(user_data):
        """Create a new user."""
        result, errors = UserService.user_schema.load(user_data)

        if errors:
            return False, errors

        if UserModel.query.filter_by(username=result['username']).first():
            return False, 'Username already exists'

        new_user = UserModel(username=result['username'], password=result['password'])
        db.session.add(new_user)
        db.session.commit()

        return True, 'User created successfully'
