from django.urls import path
from . import views

app_name = 'feedback'
urlpatterns = [
    path('create/', views.NewFeedbackView.as_view(), name="create"),
    path('create-for/<product_id>/',
         views.ProductFeedbackView.as_view(), name="product_feedback"),
    path('dialog/<product_id>/', views.Dialog.as_view(), name="dialog")
]
