from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse
from django.views.decorators.http import require_http_methods

from TimeTrack.forms import GroupForm, TodoForm
from TimeTrack.models import Group, Todo


# Create your views here.


def index(request):
    return render(request, 'TimeTrack/index.html')


@login_required
def group(request):
    group = Group.objects.filter(owner=request.user)
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


def delete_group(request, group_id):
    if request.method != 'POST':
        return redirect('TimeTrack:group')
    else:
        group = Group.objects.get(id=group_id)
        group.delete()
        return redirect('TimeTrack:group')


def delete_todo(request, todo_id):
    if request.method != 'POST':
        return redirect('TimeTrack:group')
    else:
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
        return redirect('TimeTrack:group')
