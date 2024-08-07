from django.urls import path

from . import views

app_name = 'TimeTrack'
urlpatterns = [
    path('', views.index, name='index'),
    path('group/', views.group, name='group'),
    path('new_group/', views.new_group, name='new_group'),
    path('new_todo/', views.new_todo, name='new_todo'),
    path('delete_group/<int:group_id>', views.delete_group, name='delete_group'),
    path('delete_todo/<int:todo_id>', views.delete_todo, name='delete_todo'),
    path('pomodoro', views.pomodoro, name='pomodoro'),
    path('myDay', views.myDay, name='myDay'),
    path('checkin', views.checkin, name='checkin'),
    path('new_checkin', views.new_checkin, name='new_checkin'),
    path('finish_checkin/<int:checkin_id>', views.finish_checkin, name='finish_checkin'),
    path('delete_checkin/<int:checkin_id>', views.delete_checkin, name='delete_checkin'),
]
