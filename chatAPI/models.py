from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    content_txt = models.CharField(max_length=255)
    content_img = models.ImageField(upload_to='msgs',blank=True, null=True)
    user_writer_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    REQUIRED_FIELDS = ['content_txt','user_writer_id']

    # def __str__(self):
    #     return self.content
