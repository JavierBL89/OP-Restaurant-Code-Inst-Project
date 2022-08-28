from django.db import models

# Create your models here.

class Contact(models.Model):
    
    contact_name = models.CharField(max_length=50)
    contact_email = models.EmailField(max_length=100)
    contact_comment = models.TextField()

    def __string__(self):
        return {self.name}