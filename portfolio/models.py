from django.db import models


# Create your models here.
class Resume(models.Model):
	FirstName = models.CharField(max_length=30)
	LastName = models.CharField(max_length=30)
	Age = models.IntegerField()
	Nationality = models.CharField(max_length=30)
	Freelance = models.CharField(max_length=30)
	Address = models.CharField(max_length=200)
	Phone = models.CharField(max_length=12)
	Email = models.CharField(max_length=30)
	Github = models.CharField(max_length=50)
	Languages = models.CharField(max_length=30)