from django.urls import path
from .views import (ProductDetailView,
                    ProductListView,
                    ProductSearchReasult,
                    add_product)

app_name = 'products'
urlpatterns = [
    path('all/', ProductListView.as_view(), name='all'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('category/<str:cat_slug>/', ProductListView.as_view(), name='by_category'),
    path('search/', ProductSearchReasult.as_view(), name="by_query"),
    path('create/', add_product, name='add_product'),
]
