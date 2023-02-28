from django.db import models
from django.contrib.auth.models import User

#creating a profile for the user

class Profile(models.Model):
    #choices
    name = models.CharField(max_length=200)
    gender_choices = models.TextChoices("Gender", ["male", "female"])
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=64, choices=gender_choices.choices)
    company = models.TextField()
    job = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)





    def __str__(self) -> str:
        return f"{self.name}"




