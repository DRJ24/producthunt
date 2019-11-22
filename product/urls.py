from . import views
from django.urls import include, path


urlpatterns = [
    path('create', views.create, name='create'),
    path('detail', views.create, name='detail'),
    path('', views.home, name='home'),
    ]
