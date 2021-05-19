from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_useer_with_email_successful(self):
        """Test creating a new user with email is successfull"""
        email = 'test@muadip.com'
        password = "Testpass123"
        user = get_user_model().objects.create_user(
                email=email,
                password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
