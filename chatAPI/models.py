from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    content = models.ImageField(upload_to='msgs')
    user_writer_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    REQUIRED_FIELDS = ['content','user_writer_id']

    # def __str__(self):
    #     return self.content

class LoginRegister(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.models.DecimalField()

    REQUIRED_FIELDS = ['user_id']
    # constraints = [
    #     models.UniqueConstraint(fields=['user_id'], name='unique_user')
    # ]
