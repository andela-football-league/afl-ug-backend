
from application import db
from utils.database import DatabaseUtils

access = db.Table(
    'access',
    db.Column('person_id', db.Integer, db.ForeignKey('person.person_id')),
    db.Column('permission_id', db.Integer, db.ForeignKey('permission.permission_id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.role_id'))
)

class Permission(db.Model, DatabaseUtils):
    permission_id = db.Column(db.Integer, primary_key=True)
    permission_name = db.Column(db.String(50), nullable=False)
    roles = db.relationship(
        'Role',
        secondary=access, 
        backref='permission',
        cascade='save-update,delete',
        lazy='dynamic') 

    def __repr__(self):
        return f"<Permission: {self.permission_id} {self.permission_name}>"
