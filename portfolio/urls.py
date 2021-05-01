from django.urls import path
from . import views
from .views import ProjectListView, BlogListView


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/', ProjectListView.as_view(), name='portfolio'),
    path('blog/', BlogListView.as_view(), name='blog'),
    # path('blog-post/', views.blogpost, name='blogpost'),

]