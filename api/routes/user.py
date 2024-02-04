from flask_smorest import Blueprint

from api.views.user import UserListView

user_blueprint = Blueprint('Users', 'users', url_prefix='/users')

user_blueprint.add_url_rule('', view_func=UserListView.as_view('user_list'), methods=['GET', 'POST'])
