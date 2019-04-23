from flask import jsonify, make_response
from flask.views import MethodView
from webargs.flaskparser import use_args

from api.permissions.models import Permission
from api.permissions.schema import PermissionSchema
from api.permissions.templates import permission_obj, permissions_obj
from utils import Utils


class PermissionView(MethodView):
    
    def get(self, permission_id):
        if permission_id:
            response_ = Utils.check_id(permission_id, 'Permission')
            permission = Permission.query.filter_by(permission_id=permission_id).first() if not response_ else {}

            if isinstance(permission, dict):
                response = response_
            else:
                response = Utils.return_response(permission, response_, permission_obj, 'Permission')

        else:
            permissions = Permission.query.all()
            response = {
                "result": "ok",
                "permissions": permissions_obj(permissions)
            }
        return make_response(jsonify(response), 200)
    
    @use_args(PermissionSchema(), locations=("json", "form"))
    def post(self, args):
        permission = Permission()
        for key, value in args.items():
            setattr(permission, key, value)
        permission.save()
        response = {
            "result": "ok",
            "permission": permission_obj(permission)
        }
        return make_response(jsonify(response), 201)


