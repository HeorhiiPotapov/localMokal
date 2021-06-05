from django.urls import path
from .views import (ProductDetailView,
                    ProductListView,
                    ProductSearchResult,
                    ProductDeleteView,
                    add_product,
                    get_products_qs,
                    CategoryListView)

app_name = 'products'
urlpatterns = [
    path('all/', ProductListView.as_view(), name='all'),
    path('categories/', CategoryListView.as_view(), name="categories"),
    path('category/<pk>/<cat_slug>/',
         ProductListView.as_view(), name='by_category'),
    path('detail/<int:pk>/<str:slug>/',
         ProductDetailView.as_view(), name='detail'),
    path('search-results/', ProductSearchResult.as_view(), name="by_query"),
    path('search/', get_products_qs, name="by_query_ajax"),
    path('create/', add_product, name='add_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name="delete_product")
]
