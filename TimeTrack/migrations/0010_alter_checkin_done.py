# Generated by Django 5.0.7 on 2024-08-07 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTrack', '0009_checkin_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='done',
            field=models.DateField(),
        ),
    ]