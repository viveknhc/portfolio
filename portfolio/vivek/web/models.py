from django.db import models
from ckeditor.fields import RichTextField

class PersonalDetails(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.EmailField()
    github = models.URLField(max_length=1000, blank=True, null=True)
    linkedin = models.URLField(max_length=1000, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class SkillSett(models.Model):
    skillsett =  models.CharField(max_length=500)

    def __str__(self):
        return self.skillsett

class Experience(models.Model):
    skill = models.ForeignKey(SkillSett,on_delete=models.CASCADE,null=True,blank=True)
    designation = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    fromDate = models.DateField()
    toDate = models.DateField()

    def __str__(self):
        return self.company_name

class Education(models.Model):
    college = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    fromDate = models.CharField(max_length=200)
    toDate = models.CharField(max_length=200)

    def __str__(self):
        return self.college

class Service(models.Model):
    service = models.CharField(max_length=200)

    def __str__(self):
        return self.service

class Projects(models.Model):
    project = models.CharField(max_length=200)
    description = RichTextField()
    image = models.FileField(upload_to='projects/')
    link = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.project

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = RichTextField() 

    def __str__(self):
        return self.name


# class PersonalDetails(models.Model):


#     def __str__(self):
#         return self.