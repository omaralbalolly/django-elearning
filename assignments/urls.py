from django.urls import path
from .views import assignment_page

urlpatterns = [
    path('<assignment_id>', assignment_page, name='assignment'),
]
