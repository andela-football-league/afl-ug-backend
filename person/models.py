from application import db
from utils.database import DatabaseUitls


class Person(db.Model, DatabaseUitls):
    person_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=True)
    position = db.Column(db.String(50), nullable=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.team_id'), nullable=False)

    def __repr__(self):
        return f"<Person: {self.first_name} {self.last_name}>"
