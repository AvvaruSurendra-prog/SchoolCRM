from django.test import TestCase
from users.models import CustomUser

class CustomUserCRUDTest(TestCase):
    """Test CRUD operations for CustomUser model."""

    def setUp(self):
        """Set up a test user before running tests."""
        self.user = CustomUser.objects.create_user(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            password="Test@123",
            role="student"
        )

    def test_create_user(self):
        """Test creating a regular user."""
        user = CustomUser.objects.create_user(
            first_name="Jane",
            last_name="Smith",
            email="jane.smith@example.com",
            password="Test@123",
            role="teacher"
        )
        self.assertEqual(user.first_name, "Jane")
        self.assertEqual(user.last_name, "Smith")
        self.assertEqual(user.role, "teacher")
        self.assertTrue(CustomUser.objects.filter(email="jane.smith@example.com").exists())

    def test_create_superuser(self):
        """Test creating a superuser."""
        admin = CustomUser.objects.create_superuser(
            first_name="Admin",
            last_name="User",
            email="admin@example.com",
            password="Admin@123"
        )
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)

    def test_read_user(self):
        """Test retrieving a user."""
        user = CustomUser.objects.get(email="john.doe@example.com")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.role, "student")

    def test_update_user(self):
        """Test updating a user's details."""
        self.user.first_name = "Johnny"
        self.user.save()
        updated_user = CustomUser.objects.get(email="john.doe@example.com")
        self.assertEqual(updated_user.first_name, "Johnny")

    def test_delete_user(self):
        """Test deleting a user."""
        user_count_before = CustomUser.objects.count()
        self.user.delete()
        user_count_after = CustomUser.objects.count()
        self.assertEqual(user_count_after, user_count_before - 1)
        self.assertFalse(CustomUser.objects.filter(email="john.doe@example.com").exists())
