# Generated by Django 4.0.3 on 2022-03-17 11:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_alter_content_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 17, 17, 24, 10, 540526), verbose_name='date published'),
        ),
    ]
