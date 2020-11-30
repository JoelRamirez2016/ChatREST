from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    """ Modelo para la creacion de mensajes: 
    el mensaje constara de texto y una unica imagen a adjuntar ademas del id del usuario 
    generado desde los modelos de django
     """

    content_txt = models.CharField(max_length=255)
    content_img = models.ImageField(upload_to='msgs',blank=True, null=True)
    user_writer_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    REQUIRED_FIELDS = ['content_txt','user_writer_id']

    # def __str__(self):
    #     return self.content
