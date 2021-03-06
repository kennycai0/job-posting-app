from django.db import models
from django.contrib.auth.models import User


class Vacancy(models.Model):
    objects = models.Manager()
    description = models.TextField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
