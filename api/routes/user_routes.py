from flask_smorest import Blueprint

from api.views.user_view import UserView

user_routes = Blueprint('user_routes', __name__)

user_view = UserView.as_view('user_view')
user_routes.add_url_rule('/users', view_func=user_view, methods=['GET', 'POST'])
