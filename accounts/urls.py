
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from home.views import HomeView

app_name = 'accounts'


urlpatterns = [
    
    path('register', views.register, name='register' ),
    path('profile', views.view_profile, name='view_profile'),
    path('profile/(?p<pk>d+)', views.view_profile, name='view_profile_with_pk'),
    path('profile/edit/', views.edit_profile, name='edit_profile' ),
    path('change-password', views.change_password, name="change.password"),
   
]

    
