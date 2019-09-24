from django.db import models


# Create your models here.
from django.db.models import ForeignKey


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=30)
    date_posted = models.DateTimeField
    author = models.ForeignObject

