from datetime import timedelta
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import date

from TimeTrack.forms import GroupForm, TodoForm, CheckInForm
from TimeTrack.models import Group, Todo, CheckIn


# Create your views here.


def index(request):
    return render(request, 'TimeTrack/index.html')


@login_required
def group(request):
    group = Group.objects.filter(owner=request.user)
    for g in group:
        for todo in g.todo_set.all():
            if todo.deadline < timezone.now():
                todo.is_expired = True
            else:
                todo.is_expired = False
            todo.save()
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


def pomodoro(request):
    return render(request, 'TimeTrack/pomodoro.html')


@login_required
def myDay(request):
    group = Group.objects.filter(owner=request.user)
    checkin = CheckIn.objects.filter(owner=request.user)
    checkins = []
    todos = []
    now = timezone.now()
    for icheckin in checkin:
        if icheckin.done == date(year=now.year, month=now.month, day=now.day):
            icheckin.doneToday = True
        if icheckin.start <= date(year=now.year, month=now.month,
                                  day=now.day) <= icheckin.end and not icheckin.doneToday:
            checkins.append(icheckin)
    for g in group:
        for todo in g.todo_set.all():
            if todo.deadline < timezone.now():
                todo.is_expired = True
            else:
                todo.is_expired = False
            todo.save()
            dateStart = todo.deadline
            dateEnd = dateStart + timedelta(days=1)
            if dateStart <= timezone.now() <= dateEnd:
                todos.append(todo)
    todos.sort(key=lambda t: t.importance, reverse=True)
    context = {'todos': todos, 'checkins': checkins}

    return render(request, 'TimeTrack/myDay.html', context=context)


@login_required
def checkin(request):
    checkins = CheckIn.objects.filter(owner=request.user)
    now = timezone.now()
    for checkin in checkins:
        if checkin.done == date(year=now.year, month=now.month, day=now.day):
            checkin.doneToday = True
    context = {'checkins': checkins}

    return render(request, 'TimeTrack/checkIn.html', context=context)


@login_required
def new_checkin(request):
    if request.method != 'POST':
        form = CheckInForm()
    else:
        form = CheckInForm(data=request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.owner = request.user
            new.doneToday = False
            new.done = new.start - timedelta(days=1)
            new.save()
            return redirect('TimeTrack:checkin')

    context = {'form': form}
    return render(request, 'TimeTrack/newCheckIn.html', context=context)


@login_required
def finish_checkin(request, checkin_id):
    if request.method != 'POST':
        return redirect('TimeTrack:checkin')
    else:
        checkin = CheckIn.objects.get(id=checkin_id)
        now = timezone.now()
        checkin.done = date(year=now.year, month=now.month, day=now.day)
        checkin.save()
        return redirect('TimeTrack:checkin')


@login_required
def delete_checkin(request, checkin_id):
    if request.method != 'POST':
        return redirect('TimeTrack:checkin')
    else:
        checkin = CheckIn.objects.get(id=checkin_id)
        checkin.delete()
        return redirect('TimeTrack:checkin')
