from django.urls import path

from . import views

app_name = 'TimeTrack'
urlpatterns = [
    path('', views.index, name='index'),
    path('group/', views.group, name='group')
]
