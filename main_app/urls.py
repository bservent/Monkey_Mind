from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('browse/', views.categories_browse, name='browse'),
    path('meditation/<int:meditation_id>/', views.meditation_detail, name='meditation_detail'),
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('profile/<int:user_id>/delete/', views.delete_profile, name='delete_profile'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('profile/<int:user_id>/edit/', views.edit_profile, name='edit_profile'),
    path('create_profile/<int:user_id>/', views.create_profile, name='create_profile')
]