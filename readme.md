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

```shell
# 生成中文的po文件
python manage.py makemessages -l zh_HANS
# 生成英文的po文件
python manage.py makemessages -l en
# 翻译完成后 生成mo文件
python manage.py compilemessages
```

Git和Github是两个在软件开发和团队协作中非常重要的工具，它们各自扮演着不同的角色但紧密相关。

### Git

**定义与功能**：
Git是一个开源的分布式版本控制系统，由Linus Torvalds为了帮助管理Linux内核开发而创建。它允许开发者在不同的计算机上工作，同时跟踪和管理代码的更改，这对于团队合作和项目管理尤为重要。Git的分布式特性意味着每个开发者都可以在自己的计算机上拥有一个完整的代码仓库副本，这使得代码的管理和版本控制更加灵活和高效。

**主要功能**：

* **版本控制**：记录文件的每次更新，并对每个版本进行快照或记录补丁文件。
* **分布式管理**：不同于集中式版本控制系统，Git的仓库是分布式的，无需依赖中心服务器。
* **高效协作**：支持分支操作，使得开发者可以在不干扰主分支的情况下进行功能开发或错误修复。

**基本操作流程**：

1. **安装Git**：从Git官网下载并安装。
2. **初始化仓库**：使用`git init`命令在项目目录中创建一个新的Git仓库。
3. **添加文件到暂存区**：使用`git add <file>`命令将文件添加到暂存区。
4. **提交更改**：使用`git commit -m "your message"`命令将暂存区的更改提交到本地仓库。
5. **查看状态**：使用`git status`命令查看当前仓库的状态。
6. **分支操作**：使用`git branch`、`git checkout <branch>`和`git merge <branch>`等命令进行分支的创建、切换和合并。

### Github

**定义与功能**：
Github是一个基于Web的Git仓库托管平台，它提供了代码托管、版本控制、团队协作、项目管理等功能。Github支持Git作为唯一的版本库格式，使得开发者可以方便地将代码托管在云端，并与团队成员共享和协作。

**主要功能**：

* **代码托管**：为开源和私有项目提供代码托管服务。
* **团队协作**：支持多人协作开发，包括代码审查、合并请求等功能。
* **项目管理**：提供项目看板、里程碑、任务分配等项目管理工具。
* **社区交流**：允许开发者关注他人、参与讨论组、分享代码片段等。

**基本使用流程**：

1. **注册Github账号**：访问Github官网注册一个账号。
2. **创建仓库**：登录后，点击“New”->“Repository”创建一个新的仓库。
3. **克隆仓库**：使用`git clone`命令将远程仓库克隆到本地计算机。
4. **本地开发**：在本地进行代码开发，并使用Git命令进行版本控制。
5. **推送更改**：将本地仓库的更改推送到远程Github仓库。

### 总结

Git和Github是软件开发和团队协作中不可或缺的工具。Git提供了强大的版本控制功能，使得开发者可以高效地管理代码更改；而Github则提供了基于Web的仓库托管服务，使得代码可以方便地托管在云端，并与团队成员共享和协作。两者相结合，为软件开发带来了极大的便利和效率提升。

<br><br>

下载并使用Git和Github涉及几个关键步骤，下面将分别详细介绍。

### 一、下载Git

1. **访问Git官网**：
   - 打开浏览器，访问[Git官网](https://git-scm.com/)https://git-scm.com/。

2. **下载Git**：
   - 在Git官网首页，找到并点击“Downloads”按钮。
   - 根据你的操作系统（如Windows、Mac、Linux等），选择对应的下载链接。
   - 下载完成后，找到下载的文件，并双击安装程序进行安装。
   - 安装过程中，通常只需要按照安装向导的指示进行即可，选择适合你的安装选项。

3. **验证Git安装**：
   - 安装完成后，打开命令行工具（在Windows上可以使用Git Bash，Mac和Linux上则使用Terminal）。
   - 输入`git --version`命令，如果系统返回了Git的版本号，则说明Git已成功安装。

### 二、配置Git

1. **配置用户名和邮箱**：
   - 在命令行中输入以下命令来配置你的Git用户名和邮箱地址，这些信息将用于你的Git提交记录。
     ```bash
     git config --global user.name "Your Name"
     git config --global user.email "youremail@example.com"
     ```
   - 将`Your Name`和`youremail@example.com`替换成你的实际姓名和邮箱地址。

### 三、下载并使用Github

1. **注册Github账号**：
   - 打开[Github官网](https://github.com/)。https://github.com/
   - 点击页面右上角的“Sign Up”按钮，填写相关信息注册一个Github账号。
   - 注册完成后，登录你的Github账号。

2. **使用Github Desktop（可选）**：
   - 注：本人不建议安装，其实pycharm自带了一个版本控制的界面的，根本不需要这个
   - 如果你希望使用图形界面来管理Github仓库，可以下载并安装Github Desktop。
   - 访问[Github Desktop官网](https://desktop.github.com/)https://desktop.github.com，根据你的操作系统下载并安装Github Desktop。

3. **访问和下载仓库**：
   - 登录Github后，你可以通过搜索或浏览找到感兴趣的仓库。
   - 进入仓库页面后，点击页面右上角的绿色按钮“Code”，然后选择“Download ZIP”选项来下载整个仓库的压缩包。
   - 或者，你可以使用Git命令（如`git clone`）来克隆仓库到你的本地计算机上，以便进行更深入的版本控制操作。

4. **使用Git命令管理仓库**：
   - 如果你已经克隆了仓库到本地，你可以使用Git的各种命令来管理你的代码。
   - 常用的Git命令包括`git add`（添加文件到暂存区）、`git commit`（提交更改到本地仓库）、`git push`（将更改推送到远程仓库）等。

### 四、总结

下载并使用Git和Github涉及下载Git软件、配置Git、注册Github账号、访问和下载仓库以及使用Git命令管理仓库等步骤。通过遵循上述步骤，你可以开始使用Git和Github进行版本控制和团队协作。记得在学习过程中多实践，以加深对Git和Github的理解。