from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

class History(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    
    email_from  = models.EmailField(blank = True)
    email_to    = models.TextField(blank=True)
    ip          = models.CharField(max_length=50, default='127.0.0.1')
    time        = models.DateTimeField(default=datetime.now())
