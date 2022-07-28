from django.urls import path
from .views import course_page, courses_page
urlpatterns = [
    path('courses/<course_id>', course_page, name='course'),
    path('courses/', courses_page, name='courses'),
]