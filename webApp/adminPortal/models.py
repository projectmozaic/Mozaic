from __future__ import unicode_literals

from django.db import models


# Create your models here.
class PythonPackages(models.Model):
    python27 = models.BooleanField()

class RPackages(models.Model):
    Rdist = models.BooleanField()
