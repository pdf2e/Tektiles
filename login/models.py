from django.db import models
from loginRouter import *

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    emailAddress = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


class Companion(models.Model):
    category = models.CharField(max_length=30)