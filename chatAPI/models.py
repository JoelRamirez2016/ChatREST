from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    content = models.CharField(max_length=255)
    user_writer_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    REQUIRED_FIELDS = ['content','user_writer_id']
    # def __str__(self):
    #     return self.content



