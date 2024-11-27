from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,StudentProfile, TeacherProfile

# Customizing the user admin interface
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username','is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'username')
    ordering = ('email',)

    # Include the required fields in the admin form
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
      
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2','is_staff', 'is_active'),
        }),
    )

# Register CustomUser in the admin
admin.site.register(CustomUser, CustomUserAdmin)
@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'grade_level')

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'hourly_rate')