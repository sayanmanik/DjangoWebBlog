from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name = 'blog-home'),
    path('blog/about/',views.about,name = 'blog-about'),
]