from django.db import models

# Create your models here.
class ProjectDetails(models.Model):
    projectName  = models.AutoField(primary_key=True)
    developerNames = models.CharField(max_length=1000)
    dateOfStart = models.DateField(max_length=1000)
    dateOfEnd = models.DateField(max_length=1000)
    languagesUsed = models.CharField(max_length=1000)
    projectContent = models.CharField(max_length=1000)

