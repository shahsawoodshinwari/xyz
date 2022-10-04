from django.test import Client, TestCase
from django.contrib.auth.models import User

# Create your tests here.
class TestUserAppStatus(TestCase):
    """tests status of all pages"""

    def setUp(self):
        """Every test needs a client."""
        self.client = Client()
        User.objects.create(username="test", password="password")

    def test_login_page_status(self):
        """tests the status of the landing page"""
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)

    def test_register_page_status(self):
        """tests the status of the landing page"""
        response = self.client.get("/accounts/register/")
        self.assertEqual(response.status_code, 200)

    def test_registered_users_count(self):
        """tests number of users registered"""
        users = User.objects.all()
        self.assertEqual(users.count(), 1)

    def test_logging_in(self):
        """login a user"""
        response = self.client.post(
            "/accounts/login/", {"username": "test", "password": "password"}
        )
        self.assertEqual(response.status_code, 200)
