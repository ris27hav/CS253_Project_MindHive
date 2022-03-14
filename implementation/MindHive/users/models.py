from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, AbstractUser


class UserInfoManager(BaseUserManager):
    def create_user(self, email, username, name, password,roll_no=None, ):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            username=username,
            roll_no=roll_no,
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, name=None, roll_no=None):
        user = self.create_user(email=email, username=username, name=name,
                                roll_no=roll_no, password=password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user

class User(AbstractUser):

    username = models.CharField(max_length=20,blank=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        blank=False,
    )

    name = models.CharField(max_length=20, blank=True, null=True)
    roll_no=models.CharField(max_length=8, blank=True, null=True)

    profile_image = models.ImageField(upload_to='profile_image', default='default.jpg')
    blocked = models.BooleanField(default=False)
    followingQuestions = models.ManyToManyField(to='questions.Question', related_name='users_following', blank=True)
    bookmarkQuestions = models.ManyToManyField(to='questions.Question', related_name='users_bookmarked', blank=True)
    favouriteTags = models.ManyToManyField(to='tags.Tag', blank=True)
    notifications = models.ManyToManyField(to='notifications.Notification', blank=True)


    objects = UserInfoManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username' ]

    def __str__(self):
        return self.username
class Report(models.Model):
    report_text = models.CharField(max_length=200)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    reportedUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported')
    reportedObjType = models.CharField(max_length=20)
    reportedObjQ = models.ForeignKey(to='questions.Question', on_delete=models.CASCADE, null=True, blank=True)
    reportedObjA = models.ForeignKey(to='answers.Answer', on_delete=models.CASCADE, null=True, blank=True)
    reportedObjC = models.ForeignKey(to='comments.Comment', on_delete=models.CASCADE, null=True, blank=True)
    report_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.report_text
