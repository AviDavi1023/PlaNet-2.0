from django.db import models
from django.contrib.auth.models import User

class Plant (models.Model):
    user = models.ForeignKey(User, related_name='plant', on_delete=models.CASCADE)
    name = models.CharField(blank=True, null=True, max_length=40)
    date_found = models.DateTimeField(auto_now_add=True)
    location = models.CharField(blank=True, null=True, max_length=50)
    comment = models.TextField(max_length=5000)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name