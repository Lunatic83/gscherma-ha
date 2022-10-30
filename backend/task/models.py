from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.

# New user model
class User(AbstractUser):

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

# Task model
class Task(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    # Each task 
    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title


