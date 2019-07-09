from marshmallow import Schema
from webargs import fields, validate


class PersonSchema(Schema):
    person_id = fields.Int(dump_only=True)
    first_name = fields.Str(
        required=True,
        validate=validate.Length(3),
        error_messages={"required": {"message": "First name required", "code": 400}},
    )
    last_name = fields.Str(required=True, validate=validate.Length(3))
    role = fields.Int()
    position = fields.Str(missing="")
    team_id = fields.Int()

    class Meta:
        strict = True
