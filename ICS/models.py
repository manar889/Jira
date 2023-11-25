from django.db import models

# Create your models here.
class Patient(models.Model):
     username = models.CharField(max_length=200, null=True)
     email = models.CharField(max_length=200, null=True)
     date_created = models.DateTimeField(auto_now_add=True, null= True)

     def __str__(self):
        return self.username