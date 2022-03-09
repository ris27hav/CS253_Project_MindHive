# Generated by Django 4.0.3 on 2022-03-09 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0001_initial'),
        ('tags', '0001_initial'),
        ('answers', '0002_initial'),
        ('notifications', '0002_initial'),
        ('comments', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('profile_image', models.ImageField(blank=True, upload_to='profile_image')),
                ('blocked', models.BooleanField(default=False)),
                ('bookmarkQuestions', models.ManyToManyField(related_name='user_bq', to='questions.question')),
                ('favouriteTags', models.ManyToManyField(blank=True, to='tags.tag')),
                ('followingQuestions', models.ManyToManyField(related_name='user_fq', to='questions.question')),
                ('notifications', models.ManyToManyField(blank=True, to='notifications.notification')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_text', models.CharField(max_length=200)),
                ('reportedObjType', models.CharField(max_length=20)),
                ('report_date', models.DateTimeField(auto_now_add=True)),
                ('reportedObjA', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='answers.answer')),
                ('reportedObjC', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comments.comment')),
                ('reportedObjQ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.question')),
                ('reportedUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported', to='users.user')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]