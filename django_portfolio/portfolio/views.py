# Create your views here.
from django.shortcuts import render_to_response
from django_portfolio.portfolio.models import *

def index(request):
    project_list = Project.objects.all().order_by('-project_date')
    project_year_list = {}
    for project in project_list:
        if project.project_date.year not in project_year_list.keys():
            project_year_list[project.project_date.year] = []
        project_year_list[project.project_date.year].append(project)
    project_year_list = [ (k,project_year_list[k]) for k in sorted(project_year_list.keys(), reverse=True)]
    return render_to_response('portfolio/index.html', {"project_year_list" : project_year_list})
