from django.urls import path
from . import views


app_name = 'infopages'
urlpatterns = [
    path('about/', views.AboutUsPage.as_view(), name="about_us"),
    path('about/create/', views.AboutUsPageCreate.as_view(), name="about_create"),
]
