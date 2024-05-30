from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
    shared_with = models.ManyToManyField(User, related_name='shared_collections', blank=True)

    def __str__(self):
        return self.name

class URL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
