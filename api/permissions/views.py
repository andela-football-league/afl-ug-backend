from flask import Blueprint

from api.permissions.api import PermissionView

permission_app = Blueprint("permission_app", __name__)
permission_view = PermissionView.as_view('permission_view')
permission_app.add_url_rule("/permissions/", defaults={"permission_id": None},
                        view_func=permission_view, methods=["GET"])
permission_app.add_url_rule("/permissions/", view_func=permission_view, methods=["POST"])
permission_app.add_url_rule("/permissions/<permission_id>", view_func=permission_view,
                        methods=["GET", "PUT", "DELETE"])
