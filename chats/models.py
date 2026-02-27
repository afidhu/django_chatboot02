from django.db import models

# Create your models here.

from django.db import models

class DocumentChunk(models.Model):
    content = models.TextField()
    embedding = models.JSONField()