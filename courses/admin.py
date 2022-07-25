from django.contrib import admin
from .models import Subject, Course, Enrollment
from users.models import User


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

    def description(self, obj):
        if len(obj.desc) >= 100:
            return obj.desc[:100] + '...'
        return obj.desc


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('subject', 'teacher')

    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['teacher'].queryset = User.objects.filter(
            user_type=2)  # Filter the users to get teachers only
        return super(CourseAdmin, self).render_change_form(request, context, *args, **kwargs)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course')

    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['student'].queryset = User.objects.filter(
            user_type=1)  # Filter the users to get students only
        return super(EnrollmentAdmin, self).render_change_form(request, context, *args, **kwargs)
