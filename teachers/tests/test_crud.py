from django.test import TestCase
from teachers.models import Teacher

class TeacherCRUDTest(TestCase):
    """Test CRUD operations for Teacher model."""

    def setUp(self):
        """Set up a test teacher before running tests."""
        self.teacher = Teacher.objects.create(
            name="Alice Johnson",
            subject="Mathematics",
            contact="1234567890",
            email="alice.johnson@example.com"
        )

    def test_create_teacher(self):
        """Test creating a teacher."""
        teacher = Teacher.objects.create(
            name="Bob Smith",
            subject="Physics",
            contact="9876543210",
            email="bob.smith@example.com"
        )
        self.assertEqual(teacher.name, "Bob Smith")
        self.assertEqual(teacher.subject, "Physics")
        self.assertTrue(Teacher.objects.filter(email="bob.smith@example.com").exists())

    def test_read_teacher(self):
        """Test retrieving a teacher."""
        teacher = Teacher.objects.get(email="alice.johnson@example.com")
        self.assertEqual(teacher.name, "Alice Johnson")
        self.assertEqual(teacher.subject, "Mathematics")

    def test_update_teacher(self):
        """Test updating a teacher's details."""
        self.teacher.name = "Alice J."
        self.teacher.save()
        updated_teacher = Teacher.objects.get(email="alice.johnson@example.com")
        self.assertEqual(updated_teacher.name, "Alice J.")

    def test_delete_teacher(self):
        """Test deleting a teacher."""
        teacher_count_before = Teacher.objects.count()
        self.teacher.delete()
        teacher_count_after = Teacher.objects.count()
        self.assertEqual(teacher_count_after, teacher_count_before - 1)
        self.assertFalse(Teacher.objects.filter(email="alice.johnson@example.com").exists())
