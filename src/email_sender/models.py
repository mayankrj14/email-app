from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

class History(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    
    email_from  = models.EmailField(null = True)
    email_to    = models.TextField(blank=True)

    time        = models.DateTimeField(default=datetime.now())
