from django.urls import path
from apps.accounts import views

urlpatterns = [
    path('register/', views.RegisterForm.as_view(), name='register'),
    path('login/', views.LoginForm.as_view(), name='login'),
    path('logout/', views.LogOutForm.as_view(), name='logout'),

    path('validate_username/', views.validate_username, name='validate_username'),
    path('validate_email/', views.validate_email, name='validate_email'),

    path('profile/<slug:slug>/', views.ProfileView.as_view(), name='profile'),
]
