from django.db import models

# Create your models here.

class Book(models.Model): pass
class Member(models.Model): pass
class Course(models.Model): pass
class Listing(models.Model): pass

class Book(models.Model):
    def __unicode__(self):
        return self.name
# Fields
    #bid        = models.AutoField(primary_key = True)
    owner      = models.ForeignKey(Member)
    title      = models.CharField(max_length  = 300)
    author     = models.CharField(max_length  = 100)
    editor     = models.CharField(max_length  = 10)
    isbn       = models.CharField(max_length  = 100)
    publisher  = models.CharField(max_length  = 100)
    publishDate = models.DateField()
    description= models.TextField()
    image      = models.ImageField(upload_to = "images/%Y/%m/%d")
    course     = models.ForeignKey(Course)
    price      = models.DecimalField(max_digits = 7, decimal_places = 2)


class Member(models.Model):
    def __unicode__(self):
        return self.name
# Fields
    #mid       = models.AutoField(primary_key = True)
    firstName = models.CharField(max_length  = 100)
    lastName  = models.CharField(max_length  = 100)
    email     = models.EmailField()
    password  = models.CharField(max_length  = 200)
    address   = models.CharField(max_length  = 400)
    telephone = models.CharField(max_length  = 100)

class Listing(models.Model):
    def __unicode__(self):
        return self.name
# Fields
    #lid = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 200)
    books = models.ManyToManyField(Book)

class Course(models.Model):
    def __unicode__(self):
        return self.name
# Fields
    #cid = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    department = models.CharField(max_length = 100)
    term = models.CharField(max_length = 100)


