from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None, role=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        if not first_name or not last_name:
            raise ValueError("First name and Last name are required")
        if role not in ["student", "teacher"]:
            raise ValueError("Role must be 'student' or 'teacher'")

        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email, role=role, **extra_fields)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password=None, role="teacher", **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(first_name, last_name, email, password, role, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)  # 👈 Explicitly defining the `id` field
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=[("student", "Student"), ("teacher", "Teacher")])

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"  # Users log in with email
    REQUIRED_FIELDS = ["first_name", "last_name", "role"]  # Required when using createsuperuser

    def __str__(self):
        return f"{self.id} - {self.email}"  # 👈 Displaying ID with email
