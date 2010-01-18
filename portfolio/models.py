from django.db import models

class Collaborator(models.Model):
    name = models.CharField(max_length=200)
    website_url = models.URLField()

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    website_url = models.URLField(null=True, blank=True)
    repository_url = models.URLField(null=True, blank=True)
    collaborators = models.ManyToManyField(Collaborator, null=True, blank=True)
    categories = models.ManyToManyField(Category, null=True, blank=True)
    related = models.ManyToManyField("self", null=True, blank=True)

    def __unicode__(self):
        return self.name

class MediaType(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Photo(models.Model):
    project = models.ForeignKey(Project)
    caption = models.TextField(null=True, blank=True)
    photo_url = models.URLField(null=True, blank=True)
    thumbnail_url = models.URLField(null=True, blank=True)
    flickr_url = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.project.name + ": " + self.caption

class Media(models.Model):
    projects = models.ManyToManyField(Project, null=True, blank=True)
    media_type =  models.ForeignKey(MediaType)
    description = models.TextField()
    website_url = models.TextField()

    def __unicode__(self):
        return self.media_type.name + " - " + self.description

class Press(models.Model):
    projects = models.ForeignKey(Project)
    source = models.CharField(max_length=200)
    title = models.TextField()
    website_url = models.TextField()

    def __unicode__(self):
        return self.source + " - " + self.title
