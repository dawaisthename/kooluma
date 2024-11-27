from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Progress, LessonProgress


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'progress_percentage', 'last_updated')
    list_filter = ('course', 'progress_percentage')


@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ('progress', 'lesson', 'completed', 'completion_date')
    list_filter = ('completed', 'completion_date')
