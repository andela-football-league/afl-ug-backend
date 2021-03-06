from marshmallow import Schema
from webargs import fields, validate


class PermissionSchema(Schema):
    permission_id = fields.Int(dump_only=True)
    permission_name = fields.Str(required=True, validate=validate.Length(10),
                            error_messages={'required': {'message': 'Permission name required', 'code': 400}})
    roles = fields.Nested(
        'RoleSchema',
        dump_only=True,
        many=True)

    class Meta:
        strict = True
