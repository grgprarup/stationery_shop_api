from flask_smorest import Blueprint

from api.views.user import UserListView, UserDetailView

user_blueprint = Blueprint('Users', 'users', url_prefix='/users')

user_blueprint.add_url_rule('', view_func=UserListView.as_view('user_list'), methods=['GET', 'POST'])
user_blueprint.add_url_rule('/<int:user_id>', view_func=UserDetailView.as_view('user_detail'),
                            methods=['GET', 'PUT', 'DELETE'])
