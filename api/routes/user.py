from api.views.user import UserDetail, user_blueprint
from api.views.user import UserList

user_blueprint.a.route('/users/', methods=['GET', 'POST'])(UserList)
user_blueprint.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])(UserDetail)
