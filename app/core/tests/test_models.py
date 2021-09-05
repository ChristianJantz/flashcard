from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_sucessful(self):
        """Test creating a new User with an email is successful"""
        email = "test@exsample.dev"
        password = "Testpass123"
        getUser = get_user_model()
        user = getUser.objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email address is in a Lowercase format"""
        email = "test@EXSAMPLE.DEV.DE"
        getUser = get_user_model()
        user = getUser.objects.create_user(email, 'test1234')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """
        Test the ctreate_user function, when a new user create with no email address are set
        return : ValueError
        """
        with self.assertRaises(ValueError):
            getUser = get_user_model()
            getUser.objects.create_user(None, 'test1234')

    def test_create_new_superuser(self):
        """
        Test ctreating a new superuser
        """
        getUser = get_user_model()
        user = getUser.objects.create_superuser(
            email='super@test.dev',
            password='super1234'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
