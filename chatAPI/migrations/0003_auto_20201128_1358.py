# Generated by Django 3.1.3 on 2020-11-28 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatAPI', '0002_message_user_writer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.ImageField(upload_to='msgs'),
        ),
    ]
