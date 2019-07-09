
from application import db
from utils.database import DatabaseUtils
from api.permissions.models import access


class Role(db.Model, DatabaseUtils):
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), nullable=False)
    permission_id = db.Column(db.Integer, db.ForeignKey('permission.permission_id'))
    people = db.relationship(
        'Person',
        secondary=access,
        backref='person_role',
        cascade='save-update,delete',
        lazy='dynamic'
    )
    permissions = db.relationship(
        'Permission',
        secondary=access,
        backref='permission_roles',
        cascade='save-update,delete',
        lazy='dynamic'
    )


    def __repr__(self):
        return f"<Permission: {self.role_id} {self.role_name}>"
