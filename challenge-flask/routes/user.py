from flask import Blueprint
from controllers.UserController import index, create, show, update, delete 

user_bp = Blueprint('user_bp', __name__, template_folder="/templates")
user_bp.route('/', methods=['GET'])(index)
user_bp.route('/create', methods=['POST'])(create)
user_bp.route('/<int:user_id>', methods=['GET'])(show)
user_bp.route('/update/<int:user_id>/edit', methods=['PUT'])(update)
user_bp.route('/delete/<int:user_id>', methods=['DELETE'])(delete)
