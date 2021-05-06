from django.shortcuts import render
from .models import Resume, Project, Blog
# from django.http import HttpResponse
from datetime import datetime
from django.views.generic import ListView



# Create your views here.
def home(request):
	return render(request, 'home.html')


def about(request):
	resume = Resume.objects.get(pk=1)
	number_of_projects = len(Project.objects.all())
	number_of_ml_projects = len(Project.objects.filter(ProjectType="Machine Learning"))
	number_of_dl_projects = len(Project.objects.filter(ProjectType="Deep Learning"))
	experience = round((datetime.today() - datetime(2020,11,26)).days / 30)
	return render(request, 'about.html', {"resume": resume, 
											'experience': experience,
											'nprojects':number_of_projects,
											'nmlprojects': number_of_ml_projects,
											'ndlprojects': number_of_dl_projects
										})


def contact(request):
    return render(request, 'contact.html')


# def portfolio(request):
# 	context = {
# 		'projects': Project.objects.all()
# 	}
# 	return render(request, 'portfolio.html', context)

class ProjectListView(ListView):
	model = Project	
	context_object_name = 'projects'
	template_name = "portfolio.html"
	paginate_by = 9 # pagination

class BlogListView(ListView):
	model = Blog
	context_object_name = 'blogs'
	template_name = 'blog.html'


# def blogpost(request):
# 	return render(request,'blog-post.html')