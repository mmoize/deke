from django.urls import path
from . import views
from home.views import HomeView
from django.conf.urls.static import static
from django.conf import settings

app_name ='home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('connect/<operation>.*/<int:pk>', views.change_friend, name = 'change_friends')
]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 



