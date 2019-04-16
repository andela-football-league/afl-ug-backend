from marshmallow import Schema
from webargs import fields, validate


class TeamSchema(Schema):
    team_id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(3))
    manager = fields.Int(missing=0)
    captain = fields.Int(missing=0)

    class Meta:
        strict = True
