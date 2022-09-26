from django.test import Client, TestCase

# Create your tests here.
class TestBaseAppStatus(TestCase):
    """tests status of all pages"""

    def test_landing_page(self):
        """tests the status of the landing page"""
        client = Client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
