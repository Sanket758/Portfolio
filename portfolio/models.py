from django.db import models
from django.contrib.auth.models import User


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

class Project(models.Model):
	Title = models.CharField(max_length=30)
	ProjectType = models.CharField(max_length=30)
	Client = models.CharField(max_length=30)
	Technology = models.CharField(max_length=30)
	GithubLink = models.CharField(max_length=150)
	Thumbnail = models.ImageField(upload_to='images/', )
	YoutubeLink = models.CharField(max_length=150, blank=True)

	def __str__(self):
		return self.Title