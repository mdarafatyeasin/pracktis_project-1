from django.urls import path
from . import views

urlpatterns = [
    path('', views.appHome),
    path('home', views.home),
    path('about', views.about),
    path('contact',views.contact),
]