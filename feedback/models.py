from django.db import models
from users.models import CustomUser
from courses.models import Course, Lesson

class Feedback(models.Model):
    FEEDBACK_TYPES = [
        ('course', 'Course'),
        ('lesson', 'Lesson'),
        ('teacher', 'Teacher'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='feedbacks')
    feedback_type = models.CharField(max_length=10, choices=FEEDBACK_TYPES)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, related_name='feedbacks')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True, related_name='feedbacks')
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='teacher_feedbacks')
    rating = models.PositiveIntegerField()  # Scale: 1 to 5
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.feedback_type == 'teacher':
            return f"Feedback for {self.teacher.get_full_name()} by {self.user.get_full_name()}"
        elif self.feedback_type == 'course':
            return f"Feedback for {self.course.name} by {self.user.get_full_name()}"
        elif self.feedback_type == 'lesson':
            return f"Feedback for {self.lesson.title} by {self.user.get_full_name()}"
