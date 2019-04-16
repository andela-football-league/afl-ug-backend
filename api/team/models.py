from application import db
from utils.database import DatabaseUitls


class Team(db.Model, DatabaseUitls):
    team_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    person = db.relationship('Person', backref='team', lazy=True)

    def __repr__(self):
        return f"<Team: {self.name}>"
    
    @property
    def manager(self):
        pass
    
    @property
    def captain(self):
        pass

class TeamManager(db.Model, DatabaseUitls):
    manager_id = db.Column(db.Integer, primary_key=True)
    manager = db.Column(db.Integer, db.ForeignKey('person.person_id'), nullable=False)
    captain = db.Column(db.Integer, db.ForeignKey('person.person_id'), nullable=False)
    team = db.Column(db.Integer, db.ForeignKey('team.team_id'), nullable=False)
    
