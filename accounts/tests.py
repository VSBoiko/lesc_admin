from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='sally_sal',
            email='sally001@example.com',
            password='sally_sal_001',
        )

        self.assertEqual(user.username, 'sally_sal')
        self.assertEqual(user.email, 'sally001@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@example.com',
            password='superadmin001',
        )

        self.assertEqual(user.username, 'superadmin')
        self.assertEqual(user.email, 'superadmin@example.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

