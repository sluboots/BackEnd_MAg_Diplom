from django.db import models
from user.models import Profile

# Create your models here.
class Leykocytes_Cell(models.Model):
    file = models.ImageField(upload_to='files/', null=True, max_length=255)
    target = models.BooleanField(null = True, blank=True)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
