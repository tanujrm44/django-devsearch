from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='project'),
    path('project/addproject', views.addproject, name='addproject'),
    path('project/updateproject/<str:pk>/', views.updateproject, name='updateproject'),
    path('project/deleteproject/<str:pk>/', views.deleteproject, name='deleteproject'),
]
