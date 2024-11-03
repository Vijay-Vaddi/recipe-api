"""Tests for models """

from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_email_successful(self):
        """Tests for creating user with email if success"""
        email = "vijay@example.com"
        password = "Hello123"

        user = get_user_model.objects.create_user(
            email=email, password=password)

        self.assertEqual(self.email, email)
        self.assertTrue(self.check_password(password))

