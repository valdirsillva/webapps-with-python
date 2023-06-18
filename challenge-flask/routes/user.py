from flask import Blueprint
from controllers.UserController import index # create, show, update, delete 

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(index)

# user.route('/create', methods=['POST'])(create)
# user.route('/<int:user_id>', methods=['GET'])(show)
# user.route('/update/<int:user_id>/edit', methods=['PUT'])(update)
# user.route('/delete/<int:user_id>', methods=['DELETE'])(delete)
