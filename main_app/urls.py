from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('browse/', views.categories_browse, name='browse'),
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('profile/<int:user_id>/', views.profile, name='profile')
]