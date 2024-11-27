from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=100)
    # Additional fields for language properties

class Course(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in hours")
    level = models.CharField(max_length=15, choices=LEVEL_CHOICES, default='beginner')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    content = models.TextField()
    lesson_order = models.IntegerField()  # Order in which the lesson appears
    vocabulary_list = models.TextField(blank=True, null=True)  # Optional vocabulary list

    class Meta:
        ordering = ['lesson_order']

    def __str__(self):
        return f"Lesson {self.lesson_order}: {self.title}"
