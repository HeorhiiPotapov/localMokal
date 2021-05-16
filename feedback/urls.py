from django.urls import path
from . import views

app_name = 'feedback'
urlpatterns = [
    path('create/', views.NewFeedbackView.as_view(), name="create")
]
