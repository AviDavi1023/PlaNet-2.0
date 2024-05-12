from django.db import models
from django.contrib.auth.models import User

class Plant (models.Model):
    user = models.ForeignKey(User, related_name='plant', on_delete=models.CASCADE)
    name = models.CharField(blank=True, null=True, )
    date_found = models.DateTimeField(auto_now_add=True)
    location = models.CharField(blank=True, null=True, )
    comment = description = models.CharField()

    def __str__(self):
        return self.name