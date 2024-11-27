from django.db import models

# Create your models here.
from django.db import models
from users.models import CustomUser
from courses.models import Course

class Enrollment(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  # To deactivate enrollments if needed

    class Meta:
        unique_together = ('student', 'course')  # A student can only enroll in the same course once

    def __str__(self):
        return f"{self.student.get_full_name()} enrolled in {self.course.name}"
