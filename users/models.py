from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_superuser = models.BooleanField(_('superuser status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = CustomUserManager()

    def __str__(self):
        if hasattr(self, 'student_profile'):
            return f"{self.get_full_name()} (Student)"
        elif hasattr(self, 'teacher_profile'):
            return f"{self.get_full_name()} (Teacher)"
        return self.get_full_name()  # In case it's neither, which shouldn't happen

    def get_full_name(self):
        return f"{self.first_name or ''} {self.last_name or ''}".strip()
    def save(self, *args, **kwargs):
        # Check if both profiles are present for a user and raise an error
        if hasattr(self, 'student_profile') and hasattr(self, 'teacher_profile'):
            raise ValueError("A user cannot be both a student and a teacher.")
        super().save(*args, **kwargs)

class StudentProfile(models.Model):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), max_length=50)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    grade_level = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
    def __str__(self):
        return f"{self.user.get_full_name()} (Student)"

class TeacherProfile(models.Model):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
 
    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), max_length=50)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='teacher_profile')
    specialization = models.CharField(max_length=100, blank=True, null=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"
    def __str__(self):
        return f"{self.user.get_full_name()} (Teacher) - {self.specialization or 'No Specialization'}"