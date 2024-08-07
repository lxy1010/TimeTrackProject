from django.contrib import admin

from .models import Group, Todo, CheckIn

# Register your models here.

admin.site.register(Group)
admin.site.register(Todo)
admin.site.register(CheckIn)
