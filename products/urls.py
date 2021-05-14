from django.urls import path
from .views import (ProductDetailView,
                    ProductListView,
                    ProductSearchResult,
                    add_product)

app_name = 'products'
urlpatterns = [
    path('all/', ProductListView.as_view(), name='all'),
    path('category/<cat_slug>/', ProductListView.as_view(), name='by_category'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('search/', ProductSearchResult.as_view(), name="by_query"),
    path('create/', add_product, name='add_product'),
]
