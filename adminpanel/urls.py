from django.urls import path
from . import views

app_name = 'adminpanel'
urlpatterns = [
    path('', views.MainPage.as_view(), name="main"),
    path('<int:pk>/', views.ProductUpdate.as_view(), name="edit")
]
