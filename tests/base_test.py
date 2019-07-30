import unittest
import os

from application import create_app as create_app_base, db
from api.person.models import Person
from api.team.models import Team


class BaseTestCase(unittest.TestCase):
    def create_app(self):
        return create_app_base("testing")

    def setUp(self):
        self.app_factory = self.create_app()
        self.app = self.app_factory.test_client()
        person =  Person(
            **{
                "first_name": 'xr',
                "last_name": 'cd',
                "nick_name": "ttr",
                "email": "cedriclusiba@andela.com",
                "role": 1,
                "active": True,
                "team_id": 1
            }
        )

        team = Team(
            **{
                "team_id": 1,
                "name": "zaweze"
            }
        )

        with self.app_factory.app_context():
            # create all the db tables
            db.create_all()
            team.save()
            person.save()
            db.session.commit()

    def tearDown(self):
        with self.app_factory.app_context():
            # delete all db tables
            db.session.remove()
            db.drop_all()

    def get_user_token(self):
        return os.getenv("USER_TOKEN", default=None)

    def token_headers(self):
        self.token = self.get_user_token()
        self.headers = dict(Authorization="jwt-token " + self.token)
        return self.headers
