from django.urls import path, include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('browse/', views.categories_browse, name='browse'),
    path('meditation/<int:meditation_id>/', views.meditation_detail, name='meditation_detail'),
    #path('accounts/register/', views.register, name='register'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('profile/<int:user_id>/delete/', views.delete_profile, name='delete_profile'),
    path('profile/<int:user_id>/edit/', views.edit_profile, name='edit_profile'),
    path('create_profile/', views.create_profile, name='create_profile')
]

