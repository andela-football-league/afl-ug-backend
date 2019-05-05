from tests.base_test import BaseTestCase


class TestRegisterLogin(BaseTestCase):
    def test_register(self):
        res = self.app.post("/register_login/", headers=self.token_headers())
        self.assertEqual(res.status_code, 201)
        self.assertIn("Registration successful", str(res.data))

    def test_login(self):
        self.app.post("/register_login/", headers=self.token_headers())
        res = self.app.post("/register_login/", headers=self.token_headers())
        self.assertEqual(res.status_code, 200)
        self.assertIn("Login successful", str(res.data))
    
    def test_register_without_token(self):
        res = self.app.post("/register_login/")
        self.assertEqual(res.status_code, 401)
        self.assertIn("No token. Please provide a valid token!", str(res.data))
    
    def test_register_with_invalid_token(self):
        headers = dict(Authorization="jwt-token ahsueue228383jdndn")
        res = self.app.post("/register_login/", headers=headers)
        self.assertEqual(res.status_code, 401)
        self.assertIn("Invalid token, please provide a valid token", str(res.data))
