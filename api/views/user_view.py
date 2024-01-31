from flask import jsonify, request
from flask.views import MethodView

from api.services.user_service import UserService


class UserView(MethodView):
    def get(self):
        """Get all users."""
        users = UserService.get_all_users()
        return jsonify({'users': users})

    def post(self):
        """Create a user."""
        data = request.get_json()
        result, message = UserService.create_user(data)

        if result:
            return jsonify({'message': message}), 201
        else:
            return jsonify({'message': message}), 400
