### 改进空间

1. **跨平台兼容性**：
    - 确保应用在不同浏览器（如Chrome、Firefox、Safari等）和移动设备上（通过响应式设计或开发原生应用）都能良好运行。
      ~~- 考虑使用PWA（Progressive Web App）技术，使应用能够像原生应用一样安装在用户的设备上，提高用户粘性和可用性。~~

2. **多用户与团队协作**：
    - 引入多用户系统
    - ~~允许用户创建团队并共享任务、日程等，增加协作功能。~~
      ~~- 实现权限管理，如任务分配、评论、编辑等权限的不同层级控制。~~

3. **智能提醒与通知**：
    - 集成更智能的提醒系统，如根据用户习惯或任务紧急程度自动调整提醒时间。
    - 支持多种通知方式（如邮件、短信、应用内推送），确保用户不会错过重要任务。

4. **数据可视化与报告**：
    - 提升数据统计与可视化功能，如生成任务完成率、时间分布图、效率提升报告等，帮助用户更好地分析自己的时间管理情况。
      ~~- 提供导出功能，让用户能够将报告导出为PDF、Excel等格式，便于分享或存档。~~

5. **自定义与个性化**：
    - 增加主题切换功能，让用户可以根据自己的喜好选择应用界面风格。
    - 允许用户自定义任务标签、优先级等，提高应用的灵活性和个性化程度。

6. **性能优化**：
   ~~- 对应用进行性能优化，减少加载时间，提高响应速度。~~
   ~~- 使用缓存技术，减少服务器请求，提升用户体验。~~

### 程序概述

**TimeTrack (拾光轨迹)**

**核心功能**：

- **全面升级的用户系统**：轻松跨平台使用创建个人的日程
- **智能提醒与多样化通知**：根据用户习惯和任务属性智能调整提醒时间，支持邮件、短信、应用内推送等多种通知方式，确保重要任务不遗漏。
- **深度数据统计与可视化**：提供丰富的数据统计图表和报告，如任务完成率、时间分布图、效率提升报告等，并支持导出功能，便于用户分析和分享。
- **个性化定制**：用户可根据个人喜好选择主题风格、自定义任务标签和优先级，打造专属的待办管理界面。
- **性能卓越**：经过深度优化的应用架构和Django，确保应用加载迅速、响应流畅，提升用户体验。

**特色功能**：

- **自习室模式增强**：新增白噪音、背景音乐等选项，营造更加专注的学习环境。同时，支持自定义正/倒计时时长，满足不同场景需求。
- **Pomodoro专注法优化**：引入番茄工作法的高级设置，如自定义休息时间、任务间隔等，帮助用户更科学地管理时间。
- **跨平台同步**：支持Web、iOS、Android等多平台同步，确保用户在不同设备上都能无缝衔接，随时随地管理待办事项。

**名字优点：**

1. **寓意深刻**：“拾光”二字给人以珍惜时光、捕捉美好瞬间的感觉，与待办管理和时间管理应用的核心功能相契合。“轨迹”则暗示了时间的流逝和成长的路径，符合个人成长和时间管理的主题。
2. **易于记忆**：名字简短、易于发音和记忆，这对于一个Web应用来说是非常重要的，有助于用户快速记住并传播。
3. **文化敏感性**：名字没有明显的文化冲突或负面含义，适用于广泛的受众群体。

**总结**：TimeTrack（拾光轨迹）在保留原有简约清新美观设计的基础上，通过引入多用户协作、智能提醒、深度数据统计与可视化等功能，以及性能优化和个性化定制等改进，为用户带来更加高效、智能、个性化的待办管理体验。


## 要修复的
todo增加完成标签（保留删除）

调换 done 和 doneToday （done为bool值） 将donetoday改为列表

修改 myday （todo和checkin都要改！

修复calendar（全是bug

a标签内button无效

### 最后，修复因以上更改而产生的所有Bug！

<br><br><br><br><br><br><br><br>

## 教程：如何运行服务器

### 1.进入工作目录

你的工作目录可能像这样```C:\...\TimeTrackProject\```请在文件资源管理器中打开工作目录

### 2.启动虚拟环境

按下```Win+R```启动运行，键入`cmd`以启动命令提示符

在命令提示符中键入`cd 你的工作目录`打开工作目录（你的工作目录同上）

再次键入以下命令`.\venv\Scripts\activate.bat`启动虚拟环境

画面更新并显示`(venv) C:\...\TimeTrackProject>`为成功 （这里可能不是(venv)，这取决于你的虚拟环境命名，例如：TimeTrackProject）

### 3.运行服务器

在虚拟环境中键入`python manage.py runserver`

你会看到如下输出
```shell
C:\...\TimeTrackProject\venv\Scripts\python.exe manage.py runserver 
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
August 11, 2024 - 20:25:52
Django version 5.0.7, using settings 'TimeTrackProject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

此时服务器启动成功，在浏览器中访问`http://127.0.0.1:8000/` 即可

## Bug Fix

### Bug原因

Group的排序我搞定了，其实我们都想错了，order_by其实是一个返回器方法而不是更改器方法，也就是说，objects.order_by('-importance')其实返回的是更改后的组，没有对我们操作的组进行更改

### 解决方案

既然无法更改group，我们也不能直接将这个group发送到templates，我就打算直接用迭代器来让templates访问

当然也有问题，当我打算直接迭代groups然后对每一个group的todo进行排序时出了错，于是我打算用filter限制方法来获取每个todo然后排序，当然，成功了

这是修改后的view, (当然也要对template修改，这里就不展示了)

```python
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
```
