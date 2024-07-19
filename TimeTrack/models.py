from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User


# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def cclean(self, *args, **kwargs):
        # 清除之前的验证错误
        self._errors = {}

        # 检查是否有同名的Group属于同一个User
        if Group.objects.filter(owner=self.owner, name=self.name).exclude(id=self.id).exists():
            raise ValidationError({'name': 'A group with this name already exists for this user.'})

    class Meta:
        UniqueConstraint(fields=['name', 'owner'], name='unique_group')

    def __str__(self):
        return self.name


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    done = models.BooleanField(default=False)
    importance = models.IntegerField(default=0)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['title', 'description', 'group', 'deadline', 'done', 'importance'],
                             name='unique_todo')
        ]

    def __str__(self):
        return f"{self.title}"

# python manage.py makemigrations TimeTrack
# python manage.py migrate

# 从您提供的堆栈跟踪来看，问题出现在 Group 模型的 clean 方法中，当尝试访问 self.owner 时抛出了 RelatedObjectDoesNotExist 异常。这通常意味着在调用 clean 方法时，Group 实例的 owner 属性尚未被设置或无法被访问。
#
# 然而，在您的视图 new_group 中，您已经在 form.is_valid() 调用之后设置了 new.owner = request.user。这看起来是正确的顺序，因为通常您希望在表单验证通过后才设置额外的字段（如 owner）。但是，问题可能出在 clean 方法被调用的时机。
#
# 在 Django 的 ModelForm 中，当调用 is_valid() 方法时，Django 会自动调用模型的 clean 方法以及表单的 clean 和 clean_<fieldname> 方法（如果有的话）。这意味着在表单的 is_valid() 方法内部，Django 会尝试验证模型实例，包括调用其 clean 方法。
#
# 由于 owner 字段在 GroupForm 中没有定义（因为它是一个外键，并且您只包含了 name 字段），所以在表单验证时，Group 实例的 owner 属性还没有被设置。这就是为什么在 clean 方法中访问 self.owner 时会抛出 RelatedObjectDoesNotExist 异常。
#
# 为了解决这个问题，您可以采取以下几种方法之一：
#
# 在表单中显式包含 owner 字段：
# 如果可能的话，您可以在表单中包含一个隐藏的 owner 字段，并在初始化表单时设置其值。但是，这通常不是处理外键字段的最佳方式，因为您可能不希望用户能够修改它。
# 在表单的 save 方法中设置 owner：
# 您可以在自定义的表单 save 方法中设置 owner，而不是在视图中。但是，由于您使用的是 form.save(commit=False)，这实际上不会改变 clean 方法中 owner 未被设置的问题。
# 在模型的 clean 方法中处理未设置的 owner：
# 您可以在 clean 方法中添加一个检查，以查看 owner 是否已设置，并在未设置时跳过相关验证或抛出更明确的错误。但是，这通常不是最佳实践，因为您可能希望在所有情况下都强制要求 owner。
# 在视图中处理 owner 设置：
# 由于您已经在视图中设置了 owner，并且希望在表单验证之后进行此操作，因此您可能希望将 owner 设置的逻辑移到表单验证成功之后但在调用 save() 方法之前。但是，由于 clean 方法在 is_valid() 调用期间运行，因此这仍然是一个问题。
# 重写表单的 clean 方法：
# 在表单的 clean 方法中，您可以设置 owner（如果尚未设置），然后调用模型的 clean 方法（如果需要）。但是，这通常不是处理此类问题的推荐方式，因为它将业务逻辑与表单验证混合在一起。
# 使用信号：
# 如果您希望在保存模型实例之前自动设置 owner，并且希望此逻辑与表单验证分离，则可以考虑使用 Django 的信号（如 pre_save）。但是，这通常用于在保存实例之前执行更通用的操作，而不是特定于表单验证的逻辑。
# 推荐的解决方案：
#
# 由于您已经在视图中设置了 owner，并且希望在表单验证之后进行此操作，因此最简单且最清晰的方法可能是将 owner 设置的逻辑保留在视图中，并接受在 clean 方法中可能会遇到 RelatedObjectDoesNotExist 异常的事实。但是，您可以通过在 clean 方法中添加一个检查来避免这个异常，例如：
#
# python
# def clean(self):
#     if not hasattr(self, 'owner') or self.owner is None:
#         # 如果 owner 未设置，则跳过此验证或记录日志
#         pass
#     else:
#         # 否则，执行现有的验证逻辑
#         if Group.objects.filter(owner=self.owner, name=self.name).exclude(id=self.id).exists():
#             raise ValidationError({'name': 'A group with this name already exists for this user.'})
# 但是，请注意，这实际上并不是解决问题的根本方法，因为它只是避开了异常而没有解决为什么 owner 在 clean 方法中未设置的问题。在大多数情况下，您应该确保在调用 clean 方法之前 owner 已经被正确设置。然而，在 Django 的 ModelForm 验证过程中，这通常是不可能的，因为 clean 方法是在表单验证期间由 Django 自动调用的。
