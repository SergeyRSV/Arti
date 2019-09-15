from django.urls import path

from . import views

urlpatterns = [
    path('', views.auth),
    path('send_mess/', views.send_mess),
    path('load_projects/', views.load_projects),
    path('load_members/', views.load_members),
]
