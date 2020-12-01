from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('browse/', views.browse, name='browse'),
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin')
]