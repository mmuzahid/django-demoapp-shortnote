from django.db import models
from shortnote.users.models import User


class TextNote(models.Model):
    owner = models.ForeignKey(User)
    subject = models.CharField(max_length=20)
    content = models.TextField(max_length=1024)
    remind_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
