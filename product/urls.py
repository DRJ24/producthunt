from . import views
from django.urls import include, path


urlpatterns = [
    path('create', views.create, name='create'),
    path('detaillist', views.detaillist, name='detaillist'),
    path('<int:product_id>', views.detail, name='detail'),
    path('<int:product_id>/upvote', views.upvote, name='upvote'),
    path('', views.home, name='home'),
    ]
