from django.urls import path

from . import views

app_name = 'TimeTrack'
urlpatterns = [
    path('', views.index, name='index'),
    path('group/', views.group, name='group'),
    path('new_group/', views.new_group, name='new_group'),
    path('new_todo/', views.new_todo, name='new_todo'),
]
