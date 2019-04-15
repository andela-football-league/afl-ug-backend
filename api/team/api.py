from flask import jsonify, make_response
from flask.views import MethodView
from webargs.flaskparser import use_args

from api.team.models import Team, TeamManager
from api.team.schema import TeamSchema
from api.team.templates import team_obj, teams_obj


class TeamView(MethodView):
    
    @use_args(TeamSchema(), locations=("json", "form"))
    def post(self, args):
        team = Team.query.filter_by(name=args['name']).first()
        if team:
            response = {
                "error": "Team name already taken"
            }
            return make_response(jsonify(response), 409)
        
        team = Team()
        # if args.get("manager") and args.get("captain"): 
        manager = args.get("manager")
        captain = args.get("captain")
        args.pop("manager") 
        args.pop("captain")
        for key, value in args.items():
            setattr(team, key, value)
        team.save()
        if manager and captain:
            team_manager = TeamManager(
                manager=manager,
                captain=captain,
                team=team.team_id
            )
            team_manager.save()
        response = {
            "result": "ok",
            "team": team_obj(team)
        }
        return make_response(jsonify(response), 201)
