from django.urls import path
from . import views

app_name = 'favorites'
urlpatterns = [
    path('favorite-list/', views.FavoriteListView.as_view(),
         name="favorite_list"),
    path('add_to_favorite/<product_id>/',
         views.add_to_favorite, name="add_to_favorite"),
]
