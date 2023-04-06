from django.db import models

# Create your models here.
from django.db import models

class NBAPlayer(models.Model):
    name = models.CharField(max_length=255)
    available = models.BooleanField()
