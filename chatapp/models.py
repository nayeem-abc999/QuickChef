from django.db import models

# Create your models here.
from django.db import models

class Chat(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
