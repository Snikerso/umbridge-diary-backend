# Generated by Django 3.0.3 on 2020-04-27 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200427_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dormitory',
            name='mags',
        ),
        migrations.AddField(
            model_name='dormitory',
            name='mags',
            field=models.ManyToManyField(related_name='mags', to='api.UserProgress'),
        ),
    ]
