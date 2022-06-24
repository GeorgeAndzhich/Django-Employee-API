from django.db import models

# Create your models here.
class Employee:
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=10)
    homeAddress = models.CharField(max_length=30)
    birthDate = models.DateField(null=False, blank=False)
    employmentDate = models.DateField(null=False, blank=False)