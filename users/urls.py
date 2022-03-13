"""URL patterns for users"""

from django.urls import path
from . import views


urlpatterns = [
    # Login Page
    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
]
