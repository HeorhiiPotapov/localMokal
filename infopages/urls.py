from django.urls import path
from . import views


app_name = 'infopages'
urlpatterns = [
    path('', views.AboutUsPage.as_view(), name="about_us"),
]
