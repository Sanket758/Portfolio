from django.shortcuts import render
from .models import Resume
# from django.http import HttpResponse


# Create your views here.
def home(request):
	return render(request, 'home.html')


def about(request):
	resume = Resume.objects.get(pk=1)
	return render(request, 'about.html', {"resume": resume})