from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # pic = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #デフォルトのUserクラスは使うとCustomUserを使う時に大変だから使わない

    pic = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)