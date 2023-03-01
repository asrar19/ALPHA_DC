from django.db import models

# Create your models here.



class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_comment = models.CharField(max_length=512)
