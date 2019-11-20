from . import views
from django.urls import include, path


urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

# What this says is: look for an int  AFTER /blog, and we’re going to save that as “blog_id”
# Send it to a function within the views tab (detail) that can be called on to display

    # path('<int:blog_id>/', views.blogdetail, name='detail'),


]
