# Generated by Django 3.2.12 on 2022-03-13 10:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20220313_1252'),
        ('home', '0006_auto_20220313_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='numDislikes',
        ),
        migrations.RemoveField(
            model_name='content',
            name='numLikes',
        ),
        migrations.AddField(
            model_name='content',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='content',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to='users.user'),
        ),
        migrations.AlterField(
            model_name='content',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 13, 15, 51, 59, 590687), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='content',
            name='text',
            field=models.CharField(max_length=1000),
        ),
    ]