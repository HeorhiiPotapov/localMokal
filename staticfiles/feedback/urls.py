from django.urls import path
from . import views

app_name = 'feedback'
urlpatterns = [
    path('new/', views.NewFeedbackView.as_view(), name="new")
]
