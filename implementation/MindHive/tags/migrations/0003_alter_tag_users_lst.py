# Generated by Django 4.0.3 on 2022-03-11 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220310_0515'),
        ('tags', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='users_lst',
            field=models.ManyToManyField(blank=True, related_name='favourite_of', to='users.user'),
        ),
    ]