from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    done = models.BooleanField(default=False)
    importance = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"


# python manage.py makemigrations TimeTrack
# python manage.py migrate
