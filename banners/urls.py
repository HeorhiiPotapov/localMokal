from django.urls import path
from . import views

app_name = 'banners'
urlpatterns = [
    path('', views.BannerListView.as_view(), name='banners_list'),
]
