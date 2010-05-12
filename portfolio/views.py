# Create your views here.
from django.shortcuts import render_to_response
from django.conf import settings
from np_portfolio.portfolio.models import *
import string
import os
import re
import markdown

def index(request):
    project_list = Project.objects.all().order_by('-date')
    project_year_list = {}
    project_content_list = []
    for project in project_list:
        if project.date.year not in project_year_list.keys():
            project_year_list[project.date.year] = []
        project_year_list[project.date.year].append(project)
        #content_file = os.path.join(settings.PORTFOLIO_CONTENT_PATH, str(project.short_name), 'articles', 'description.markdown')
        #if os.path.isfile(content_file):
        project_content_list.append(project.short_name)
    project_year_list = [ (k,project_year_list[k]) for k in sorted(project_year_list.keys(), reverse=True)]
    return render_to_response('portfolio/index.html', {"project_year_list" : project_year_list, "project_content_list" : project_content_list})

def project(request, project_name):
    project = Project.objects.get(short_name=project_name)
    related_projects = Project.objects.filter(related=project.id)
    press_links = Press.objects.filter(projects=project.id)
    media_links = Media.objects.filter(projects=project.id)
    photo_links = Photo.objects.filter(project=project.id)
    content_body = None
    article_path = os.path.join(settings.PORTFOLIO_CONTENT_PATH, str(project.short_name), 'articles')
    desc_file = os.path.join(article_path, 'description.markdown')
    if os.path.isfile(desc_file):
        with open(desc_file, "r") as f:
            content_body = markdown.markdown(f.read())
    articles = []
    for (root, dirs, files) in os.walk(article_path):
        for f in files:
            if os.path.splitext(f)[-1] == ".markdown":
                # parse the article name from the filename
                filename = os.path.split(f)[-1]
                urlname = " ".join(os.path.splitext(filename)[0].split("-")) #" ".join("-".split(os.path.splitext(filename)[0]))                
                urltitle = string.capwords(urlname)
                articles.append({"name": urltitle,"filepath": "/".join([project.short_name,"articles",os.path.splitext(filename)[0]])})

    description = project.description
    if project.description_long is not None:
        description = markdown.markdown(project.description_long)

    photo_thumbnails = {}
    for photo in photo_links:
        if photo.flickr_url is not None:
            photo.photo_url = photo.flickr_url
            photo.thumbnail_url = re.sub(r'.jpg', r'_t.jpg', photo.flickr_url)
    return render_to_response('portfolio/project.html', {"project" : project, "desc": description, "press_links": press_links, "media_links": media_links, "photo_links": photo_links, "photo_thumbnails": photo_thumbnails, "related_projects": related_projects, "articles": articles,  "content_body": content_body })

def article(request, project_name, article_name):
    project = Project.objects.get(short_name=project_name)
    article_filename = ".".join([article_name, "markdown"])
    article_path = os.path.join(settings.PORTFOLIO_CONTENT_PATH, str(project.short_name), 'articles', article_filename)
    if os.path.isfile(article_path):
        with open(article_path, "r") as f:
            content_body = markdown.markdown(f.read())
    return render_to_response('portfolio/article.html', {"project" : project, "content_body": content_body })

