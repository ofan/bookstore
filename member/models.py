from django.db import models

# Create your models here.

class Member(models.Model):
    def __unicode__(self):
        return self.email
# Fields
    first_name = models.CharField(max_length  = 100)
    last_name  = models.CharField(max_length  = 100)
    email     = models.EmailField()
    password  = models.CharField(max_length  = 200)

