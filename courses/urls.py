from django.urls import path
from .views import course_page, test, courses_page
urlpatterns = [
    path('course/<course_id>', course_page, name='course'),
    path('courses/', courses_page, name='courses'),
    path('test', test)
]