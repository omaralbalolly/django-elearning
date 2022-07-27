from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path("logout/", logout_view, name="logout"),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', profile_edit_view, name='profile_edit'),
    path('profile/change_password/', password_change_view, name='password_change'),
]
