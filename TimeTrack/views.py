from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from TimeTrack.forms import GroupForm, TodoForm
from TimeTrack.models import Group


# Create your views here.


def index(request):
    return render(request, 'TimeTrack/index.html')


@login_required
def group(request):
    group = Group.objects.filter(owner=request.user).order_by('todo__importance')
    context = {'group': group}
    return render(request, 'TimeTrack/group.html', context=context)


@login_required
def new_group(request):
    if request.method != 'POST':
        form = GroupForm()
    else:
        form = GroupForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.owner = request.user
            new.cclean()
            new.save()
            return redirect('TimeTrack:group')

    context = {'form': form}
    return render(request, 'TimeTrack/newGroup.html', context=context)


@login_required
def new_todo(request):
    if request.method != 'POST':
        form = TodoForm(user=request.user)
    else:
        form = TodoForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('TimeTrack:group')

    context = {'form': form}
    return render(request, 'TimeTrack/newTodo.html', context=context)
