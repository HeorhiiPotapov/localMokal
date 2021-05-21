from django.urls import path
from .views import LinksListView

app_name = 'sociallinks'
urlpatterns = [
    path('list/', LinksListView.as_view(), name='list')
]
