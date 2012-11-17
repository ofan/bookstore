from django.db import models

# Create your models here.

class Member(models.Model):
    def __unicode__(self):
        return self.email
# Fields
    #mid       = models.AutoField(primary_key = True)
    firstName = models.CharField(max_length  = 100)
    lastName  = models.CharField(max_length  = 100)
    email     = models.EmailField()
    password  = models.CharField(max_length  = 200)
    address   = models.CharField(max_length  = 400)
    telephone = models.CharField(max_length  = 100)
    books     = models.ManyToManyField('book.Book')

