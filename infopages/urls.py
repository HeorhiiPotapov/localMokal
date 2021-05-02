from django.urls import path
from . import views


app_name = 'infopages'
urlpatterns = [
    path('', views.InfoPages)
]
