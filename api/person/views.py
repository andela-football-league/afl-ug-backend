from flask import Blueprint

from api.person.api import PersonView, RegisterLoginView

person_app = Blueprint("person_app", __name__)
person_view = PersonView.as_view("person_view")
register_login_view = RegisterLoginView.as_view("register_login_view")
person_app.add_url_rule(
    "/persons/", defaults={"person_id": None}, view_func=person_view, methods=["GET"]
)
person_app.add_url_rule("/persons/", view_func=person_view, methods=["POST"])
person_app.add_url_rule(
    "/persons/<person_id>", view_func=person_view, methods=["GET", "PUT", "DELETE"]
)
person_app.add_url_rule(
    "/register_login/", view_func=register_login_view, methods=["POST"]
)
