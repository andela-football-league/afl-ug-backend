from tests.base_test import BaseTestCase
from api.roles.models import Role
import json


class TestRolesApp(BaseTestCase):
    data = json.dumps({"permission_name": "admin-has-allrights"})

    def post_get_roles(self, role=False):
        
        res = self.app.post("/permissions/", headers=self.token_headers(), data=self.data)
        permission = json.loads(self.app.get("/permissions/").data)
        permission_id = permission['permissions'][0]['permission_id']
        role_ = json.dumps({"role_name": "Admin", "permission_id": permission_id})
        res2 = self.app.post("/roles/", headers=self.token_headers(), data=role_) if not role else None


        return role_ if role else self.app.get("/roles/")


    def test_create_roles(self):
        data = self.post_get_roles(role=True)
        res = self.app.post("/roles/", headers=self.token_headers(), data=data)
        self.assertEqual(res.status_code, 201)
        self.assertIn("result", str(res.data))

    def test_get_roles(self):
        role = json.loads(self.post_get_roles().data)
        res = self.app.get(f"/roles/{role['roles'][0]['role_id']}", headers=self.token_headers())
        self.assertEqual(res.status_code, 200)
        self.assertIn("permission", str(res.data))
    