from django.db import models

# Create your models here.
class Workplan(models.Model):
    name=models.CharField('file name',max_length=200,null=True,blank=True)
    owner=models.CharField('Owner',max_length=200,null=True,blank=True)
    pdf=models.FileField(upload_to='uploads',null=True,blank=True)
    cover=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.owner

class Partner(models.Model):
    name=models.CharField('Organization Name',max_length=200,null=True,blank=True)
    logo=models.CharField('logo',max_length=300,null=True,blank=True)
    website=models.URLField('website link',max_length=300, null=True,blank=True)
    bio=models.TextField()
    headquater=models.CharField('Headquater',max_length=200,null=True,blank=True)
    image=models.ImageField('Organization logo',blank=True,null=True)

    def __str__(self):

        return self.name
class WorkplanUpdated(models.Model):
    activity_name=models.CharField('Activity Name',max_length=200,null=True,blank=True)
    responsible=models.CharField('Responsible',max_length=300,null=True,blank=True)
    implimentation=models.CharField('implimentation',max_length=300, null=True,blank=True)

    def __str__(self):
        return self.activity_name
    
    