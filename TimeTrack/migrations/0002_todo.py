# Generated by Django 5.0.7 on 2024-07-17 06:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTrack', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('deadline', models.DateTimeField()),
                ('done', models.BooleanField(default=False)),
                ('importance', models.IntegerField(default=0)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TimeTrack.group')),
            ],
        ),
    ]