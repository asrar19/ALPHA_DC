from django.db import models

# Create your models here.

# THE FEEDBACK MODEL IN CONTACT PAGE

class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_comment = models.CharField(max_length=512)
    subject = models.CharField(max_length=512)
