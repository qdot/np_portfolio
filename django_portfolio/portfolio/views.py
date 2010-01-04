# Create your views here.
from django.shortcuts import render_to_response
from django_portfolio.portfolio.models import *
import re

def index(request):
    project_list = Project.objects.all().order_by('-date')
    project_year_list = {}
    for project in project_list:
        if project.date.year not in project_year_list.keys():
            project_year_list[project.date.year] = []
        project_year_list[project.date.year].append(project)
    project_year_list = [ (k,project_year_list[k]) for k in sorted(project_year_list.keys(), reverse=True)]
    return render_to_response('portfolio/index.html', {"project_year_list" : project_year_list})

def project(request, project_name):
    project = Project.objects.get(short_name=project_name)
    related_projects = Project.objects.filter(related=project.id)
    press_links = Press.objects.filter(projects=project.id)
    media_links = Media.objects.filter(projects=project.id)
    photo_links = Photo.objects.filter(project=project.id)
    photo_thumbnails = {}
    for photo in photo_links:
        if photo.flickr_url is not None:
            photo.photo_url = photo.flickr_url
            photo.thumbnail_url = re.sub(r'.jpg', r'_t.jpg', photo.flickr_url)
    return render_to_response('portfolio/project.html', {"project" : project, "press_links": press_links, "media_links": media_links, "photo_links": photo_links, "photo_thumbnails": photo_thumbnails, "related_projects": related_projects})
