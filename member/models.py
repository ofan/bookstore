from django.db import models

# Create your models here.

class Member(models.Model):
    def __unicode__(self):
        return self.email
# Fields
    userName  = models.CharField(max_length  = 50)
    firstName = models.CharField(max_length  = 100)
    lastName  = models.CharField(max_length  = 100)
    email     = models.EmailField()
    password  = models.CharField(max_length  = 200)
    address   = models.CharField(max_length  = 400)
    telephone = models.CharField(max_length  = 100)

