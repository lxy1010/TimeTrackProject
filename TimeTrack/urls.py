from django.urls import path

from . import views

app_name = 'TimeTrack'
urlpatterns = [
    path('', views.index, name='index'),
    # Group
    path('group/', views.group, name='group'),
    path('new_group/', views.new_group, name='new_group'),
    path('delete_group/<int:group_id>', views.delete_group, name='delete_group'),
    # Tod0
    path('new_todo/', views.new_todo, name='new_todo'),
    path('delete_todo/<int:todo_id>', views.delete_todo, name='delete_todo'),
    path('done_todo/<int:todo_id>', views.done_todo, name='done_todo'),
    # Checkin
    path('checkin', views.checkin, name='checkin'),
    path('new_checkin', views.new_checkin, name='new_checkin'),
    path('finish_checkin/<int:checkin_id>', views.finish_checkin, name='finish_checkin'),
    path('delete_checkin/<int:checkin_id>', views.delete_checkin, name='delete_checkin'),
    # Others
    path('calendar', views.calendar, name='calendar'),
    path('pomodoro', views.pomodoro, name='pomodoro'),
    path('myDay', views.myDay, name='myDay'),
]
