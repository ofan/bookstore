from django.db import models

class Listing(models.Model):
    def __unicode__(self):
        return self.course
# Fields
    #bid        = models.AutoField(primary_key = True)
    email      = models.ForeignKey('member.Member')
    description= models.TextField()
    course     = models.CharField(max_length=100)
