from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (SignUpView,
                    ActivationView,
                    profile,
                    CustomPasswordChangeView)


app_name = 'users'
urlpatterns = [
    path('new/', SignUpView.as_view(), name='new'),
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='users/logout.html'), name="logout"),
    path('profile/', profile, name="profile"),
    path('activate/<uidb64>/<token>/',
         ActivationView.as_view(), name='activate'),
    path('passwd-change/',
         CustomPasswordChangeView.as_view(), name='passwd_change'),
]
