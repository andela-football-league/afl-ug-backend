from marshmallow import Schema
from webargs import fields, validate


class RoleSchema(Schema):
    role_id = fields.Int(dump_only=True)
    role_name = fields.Str(required=True, validate=validate.Length(4),
                            error_messages={'required': {'message': 'Permission name required', 'code': 400}})
    permission_id = fields.Int(required=False)
    permissions = fields.Nested(
        'PermissionSchema',
        dump_only=True,
        many=True)
    people = fields.Nested(
        'PersonSchema',
        dump_only=True,
        many=True)

    class Meta:
        strict = True
