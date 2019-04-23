
from application import db
from utils.database import DatabaseUtils


class Permission(db.Model, DatabaseUtils):
    permission_id = db.Column(db.Integer, primary_key=True)
    permission_name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Permission: {self.permission_id} {self.permission_name}>"
