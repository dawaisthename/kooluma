from django.db import models

# Create your models here.
from django.db import models
from users.models import CustomUser
from courses.models import Course, Lesson  


class Progress(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="progress_records")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="progress_records")
    progress_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('student', 'course')  # Ensures a student can't have multiple progress entries for the same course

    def __str__(self):
        return f"{self.student.get_full_name()} - {self.course.name} ({self.progress_percentage}%)"
class LessonProgress(models.Model):
    progress = models.ForeignKey(Progress, on_delete=models.CASCADE, related_name="lesson_progress_records")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="lesson_progress_records")
    completed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('progress', 'lesson')  # A student-course combination can have only one record per lesson

    def __str__(self):
        return f"{self.progress.student.get_full_name()} - {self.lesson.title} ({'Completed' if self.completed else 'In Progress'})"
