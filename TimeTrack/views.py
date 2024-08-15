from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import date, timedelta, datetime

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
    orderedGroups = {}
    for g in group:
        orderedGroups[g] = list(Todo.objects.filter(group=g).order_by('-importance'))
    context = {'group': orderedGroups}

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


def done_todo(request, todo_id):
    if request.method != 'POST':
        return redirect('TimeTrack:group')
    else:
        todo = Todo.objects.get(id=todo_id)
        todo.done = True
        todo.save()
        return redirect("TimeTrack:group")


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
        if icheckin.doneToday == date(year=now.year, month=now.month, day=now.day):
            icheckin.done = True
        if icheckin.start <= date(year=now.year, month=now.month,
                                  day=now.day) <= icheckin.end and not icheckin.done:
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
        if checkin.doneToday == date(year=now.year, month=now.month, day=now.day):
            checkin.done = True
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
            new.done = False
            new.doneToday = new.start - timedelta(days=1)
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
        checkin.doneToday = date(year=now.year, month=now.month, day=now.day)
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


def calendar(request):
    now_date = timezone.now().date()
    # 创建一个表示下个月第一天的datetime对象
    # 通过将给定日期的年份、月份加1，并将日期设置为1来实现
    next_month_first_day = datetime(now_date.year + (now_date.month == 12), now_date.month % 12 + 1, 1)

    # 然后计算这个月第一天的日期与下个月第一天的日期之间的时间差（以天为单位）
    # 减去1天，因为timedelta计算的是两个时间点之间的完整时间间隔，包括开始但不包括结束
    days_in_month = (next_month_first_day - timedelta(days=1)).day

    first_day_of_month = now_date.replace(day=1)
    weekday_of_first_day = first_day_of_month.weekday()

    now = timezone.now().date()
    days = ['' for i in range(weekday_of_first_day+1)] + [i+1 for i in range(days_in_month)]

    context = {'today': now.strftime('%B'), 'days': days}

    return render(request, 'TimeTrack/Calendar.html', context=context)
