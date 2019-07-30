from tests.base_test import BaseTestCase
from api.person.models import Person
from api.team.models import Team


class TestGetUpdatePerson(BaseTestCase):
    def test_get_persons(self):
        res = self.app.get("/persons/")
        self.assertEqual(res.status_code, 200)
        self.assertIn("persons", str(res.data))

    def test_get_person(self):

        res = self.app.get("/persons/1", headers=self.token_headers())
        self.assertEqual(res.status_code, 200)
        self.assertIn("person", str(res.data))
