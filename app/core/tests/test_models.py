from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email(self):
        """ test creating user with email address """
        email = "tester@mail.com"
        password = "testpassword"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password), password)

    def test_normalize_user_email(self):
        """ test normalizing user email address """
        email = "tester@MAILBOX.COM"
        password = "testpassword"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_invalid_email(self):
        """ test invalid email address """
        password = "testpassword"

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, password)

    def test_create_superuser(self):
        """ test create super user """

        email = "tester@MAILBOX.COM"
        password = "testpassword"
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        self.assertTrue(user.is_superuser, True)
        self.assertTrue(user.is_staff, True)
