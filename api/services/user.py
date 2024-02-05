from api.schemas.user import UserSchema
from api.models.user import UserModel
from db import db


class UserService:
    user_schema = UserSchema()

    @staticmethod
    def get_all_users():
        """Get all users"""
        users = UserModel.query.all()
        return users

    @staticmethod
    def create_user(user_data):
        print(user_data)
        """Create a new user."""
        if UserModel.query.filter_by(UserModel.username == user_data['username']).first():
            return {'message': 'Username already exists'}, 409

        user = UserModel(username=user_data['username'], password=user_data['password'])
        db.session.add(user)
        db.session.commit()

        return {'message': 'User created successfully'}, 201

    @staticmethod
    def get_user_by_id(user_id):
        user = UserModel.query.filter(UserModel.id == user_id).first()
        return UserService.user_schema.dump(user)

    @staticmethod
    def update_user_by_id(user_id, data):
        pass

    @staticmethod
    def delete_user_by_id(user_id):
        pass
