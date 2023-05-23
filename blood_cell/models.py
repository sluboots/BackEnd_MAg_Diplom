from django.db import models
from user.models import Profile

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)
# Create your models here.
class Blood_Cell(models.Model):
    file = models.ImageField(upload_to=upload_to, null=True, max_length=255)
    target = models.BooleanField(null = True, blank=True)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)

