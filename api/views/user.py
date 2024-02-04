from flask import jsonify, request
from flask.views import MethodView

from api.services.user import UserService
from api.schemas.user import UserSchema


class UserListView(MethodView):
    @staticmethod
    def get():
        """Get all users."""
        users = UserService.get_all_users()
        return jsonify({'users': users})

    @staticmethod
    def post():
        """Create a user."""
        data = request.get_json()
        result, message = UserService.create_user(data)

        if result:
            return jsonify({'message': message}), 201
        else:
            return jsonify({'message': message}), 400


class UserDetailView(MethodView):
    def get(self, user_id):
        """Get a user."""
        user = UserService.get_user(user_id)

        if user:
            return jsonify({'user': user})
        else:
            return jsonify({'message': 'User not found'}), 404

    def put(self, user_id):
        """Update a user."""
        data = request.get_json()
        result, message = UserService.update_user(user_id, data)

        if result:
            return jsonify({'message': message})
        else:
            return jsonify({'message': message}), 400

    def delete(self, user_id):
        """Delete a user."""
        result, message = UserService.delete_user(user_id)

        if result:
            return jsonify({'message': message})
        else:
            return jsonify({'message': message}), 400