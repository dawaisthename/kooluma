from django.contrib import admin

from .models import Course, Lesson, Language

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'language', 'duration')
    search_fields = ('name', 'description')
    list_filter = ('level', 'language')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'lesson_order')
    search_fields = ('title', 'content')

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)
