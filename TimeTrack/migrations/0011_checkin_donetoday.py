# Generated by Django 5.0.7 on 2024-08-07 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTrack', '0010_alter_checkin_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='doneToday',
            field=models.BooleanField(default=False),
        ),
    ]
