# Generated by Django 3.0.5 on 2020-07-08 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0010_billboard_medium'),
    ]

    operations = [
        migrations.AddField(
            model_name='billboard',
            name='Company',
            field=models.CharField(default='', max_length=60),
        ),
    ]