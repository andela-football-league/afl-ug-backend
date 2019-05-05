import unittest
import os

from application import create_app as create_app_base, db


class BaseTestCase(unittest.TestCase):
    def create_app(self):
        return create_app_base("testing")

    def setUp(self):
        self.app_factory = self.create_app()
        self.app = self.app_factory.test_client()

        with self.app_factory.app_context():
            # create all the db tables
            db.create_all()
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
