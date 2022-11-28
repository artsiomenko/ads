from django.contrib.auth.models import User
from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    rubric = models.ForeignKey('Rubric', on_delete=models.PROTECT, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True)

    def __str__(self):
        return self.name

