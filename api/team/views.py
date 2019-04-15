from flask import Blueprint

from api.team.api import TeamView

team_app = Blueprint("team_app", __name__)
team_view = TeamView.as_view("team_view")
team_app.add_url_rule("/teams/", defaults={"team_id": None},
                      view_func=team_view, methods=["GET"])
team_app.add_url_rule("/teams/", view_func=team_view, methods=["POST"])
