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

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users"""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'Test3@example.com'],
            ['test2@example.COM','test4@example.com']
        ]

        for email, expected_email in sample_emails:
            user = get_user_model().objects.create_user(email, 'hello123')
            self.assertEqual(user.email, expected_email)