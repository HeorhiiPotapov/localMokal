from django.urls import path
from . import views

app_name = "subscribes"
urlpatterns = [
    path('', views.SubscribeView.as_view(), name="create"),
]
