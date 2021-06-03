# main url config file
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from products.views import MainPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('subscribes/', include('subscribes.urls', namespace='subscribes')),
    path('favorites/', include('favorites.urls', namespace='favorites')),
    path('infopages/', include('infopages.urls', namespace='infopages')),
    path('feedback/', include('feedback.urls', namespace="feedback")),
    path('products/', include('products.urls', namespace='products')),
    path('links/', include('sociallinks.urls', namespace="sociallinks")),
    path('adminpanel/', include('adminpanel.urls', namespace="adminpanel")),
    # ################  password_reset #####################

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/passwd/reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/passwd/reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/passwd/reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/passwd/reset_complete.html'),
         name='password_reset_complete'),

    # ################ end password_reset ##################
    path('__debug__/', include(debug_toolbar.urls)),

    path('', MainPageView.as_view(), name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
