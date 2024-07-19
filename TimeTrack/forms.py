from django import forms

from .models import Group, Todo


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']
        labels = {'name': ''}


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['group', 'title', 'description', 'deadline', 'importance']
        # labels = {'title': '', 'description': ''}
        # widgets = {'description': forms.TextInput(attrs={'cols': 80})}
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            # 或者，如果不需要时间部分，可以使用：
            # 'my_datetime_field': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TodoForm, self).__init__(*args, **kwargs)
        if user and user.is_authenticated:
            self.fields['group'].queryset = Group.objects.filter(owner=user)
