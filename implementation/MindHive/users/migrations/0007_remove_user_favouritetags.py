# Generated by Django 3.2.12 on 2022-03-12 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_password_alter_user_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favouriteTags',
        ),
    ]