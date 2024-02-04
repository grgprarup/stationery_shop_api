from flask import jsonify, request
from flask.views import MethodView

from api.services.user import UserService


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
