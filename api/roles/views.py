from flask import Blueprint

from api.roles.api import RoleView

role_app = Blueprint("role_app", __name__)
role_view = RoleView.as_view('role_view')
role_app.add_url_rule("/roles/", defaults={"role_id": None},
                        view_func=role_view, methods=["GET"])
role_app.add_url_rule("/roles/", view_func=role_view, methods=["POST"])
role_app.add_url_rule("/roles/<role_id>", view_func=role_view,
                        methods=["GET", "PUT", "DELETE"])
