from django.shortcuts import render

from TimeTrack.models import Group


# Create your views here.


def index(request):
    return render(request, 'TimeTrack/index.html')


def group(request):
    group = Group.objects.order_by('todo__importance')
    context = {'group': group}
    return render(request, 'TimeTrack/group.html', context=context)
