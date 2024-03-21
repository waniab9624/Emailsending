# emails/models.py

from django.db import models

class EmailTemplate(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()

class Recipient(models.Model):
    email = models.EmailField()
    # Add more fields as needed, such as name, demographics, etc.
