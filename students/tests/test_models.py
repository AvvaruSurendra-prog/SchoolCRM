from django.test import TestCase
from students.models import Student

class StudentCRUDTest(TestCase):
    """Test CRUD operations for Student model."""

    def setUp(self):
        """Set up a test student before running tests."""
        self.student = Student.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            date_of_birth="2005-06-15",
            is_active=True
        )

    def test_create_student(self):
        """Test creating a student."""
        student = Student.objects.create(
            first_name="Jane",
            last_name="Smith",
            email="jane.smith@example.com",
            date_of_birth="2004-09-20",
            is_active=True
        )
        self.assertEqual(student.first_name, "Jane")
        self.assertEqual(student.last_name, "Smith")
        self.assertTrue(Student.objects.filter(email="jane.smith@example.com").exists())

    def test_read_student(self):
        """Test retrieving a student."""
        student = Student.objects.get(email="john.doe@example.com")
        self.assertEqual(student.first_name, "John")
        self.assertEqual(student.last_name, "Doe")

    def test_update_student(self):
        """Test updating a student's details."""
        self.student.first_name = "Johnny"
        self.student.save()
        updated_student = Student.objects.get(email="john.doe@example.com")
        self.assertEqual(updated_student.first_name, "Johnny")

    def test_delete_student(self):
        """Test deleting a student."""
        student_count_before = Student.objects.count()
        self.student.delete()
        student_count_after = Student.objects.count()
        self.assertEqual(student_count_after, student_count_before - 1)
        self.assertFalse(Student.objects.filter(email="john.doe@example.com").exists())
