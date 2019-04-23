from tests.base_test import BaseTestCase
from api.permissions.models import Permission
import json


class TestPermissionsApp(BaseTestCase):
    data = json.dumps({"permission_name": "admin2-has-allrights"})

    def post_get_permission(self):
        res = self.app.post("/permissions/", headers=self.token_headers(), data=self.data)
        return self.app.get("/permissions/")


    def test_create_permission(self):
        data = json.dumps({"permission_name": "admin2-has-allrights"})
        res = self.app.post("/permissions/", headers=self.token_headers(), data=data)
        self.assertEqual(res.status_code, 201)
        self.assertIn("result", str(res.data))

    def test_get_permission(self):
        permission = json.loads(self.post_get_permission().data)
        res = self.app.get(f"/permissions/{permission['permissions'][0]['permission_id']}", headers=self.token_headers())
        self.assertEqual(res.status_code, 200)
        self.assertIn("permission", str(res.data))
    