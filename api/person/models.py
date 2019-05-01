from application import db
from utils.database import DatabaseUtils


class Person(db.Model, DatabaseUtils):
    person_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    role = db.Column(db.Integer, nullable=True)
    picture = db.Column(db.String(255), nullable=True)
    active = db.Column(db.Boolean, default=False)
    team_id = db.Column(db.Integer, db.ForeignKey("team.team_id"), nullable=True)
    profile = db.relationship("PersonProfile", backref="person", lazy=True)

    def __repr__(self):
        return f"<Person: {self.first_name} {self.last_name}>"


class PersonProfile(db.Model, DatabaseUtils):
    profile_id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.Integer, nullable=True)
    position = db.Column(db.String(50), nullable=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.person_id"), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey("team.team_id"), nullable=False)
