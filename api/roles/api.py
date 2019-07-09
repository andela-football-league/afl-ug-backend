from flask import jsonify, make_response
from flask.views import MethodView
from webargs.flaskparser import use_args

from api.roles.models import Role
from api.roles.schema import RoleSchema
from api.roles.templates import role_obj, roles_obj
from utils import Utils


class RoleView(MethodView):
    
    def get(self, role_id):
        if role_id:
            response_ = Utils.check_id(role_id, 'Role')
            role = Role.query.filter_by(role_id=role_id).first() if not response_ else {}

            if isinstance(role, dict):
                response = response_
            else:
                response = Utils.return_response(role, response_, role_obj, 'Role')

        else:
            roles = Role.query.all()
            response = {
                "result": "ok",
                "roles": roles_obj(roles)
            }
        return make_response(jsonify(response), 200)
    
    @use_args(RoleSchema(), locations=("json", "form"))
    def post(self, args):
        role = Role()
        for key, value in args.items():
            setattr(role, key, value)
        role.save()
        response = {
            "result": "ok",
            "role": role_obj(role)
        }
        return make_response(jsonify(response), 201)


