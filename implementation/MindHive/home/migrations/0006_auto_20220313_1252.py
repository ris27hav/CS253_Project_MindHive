# Generated by Django 3.2.12 on 2022-03-13 07:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_merge_20220313_1244'),
        ('home', '0005_alter_content_author_alter_content_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='users.user'),
        ),
        migrations.AlterField(
            model_name='content',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 13, 12, 52, 21, 648374), verbose_name='date published'),
        ),
    ]