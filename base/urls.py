from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_list),
    path('join/', views.join),
    path('sport_gallery/', views.sport_gallery),
    path('gallery_list/', views.gallery_list),
    path('gallery_details/<str:player>/', views.gallery_details),
    path('update/<str:player>/', views.update_gallery),
    path('delete/<str:player>/', views.delete_gallery),
    path('teams/', views.teams),
    path('team_details/<str:team_name>/', views.team_details),
    path('team/<str:team_name>/', views.update_team),
]
