from django.db import models

# Create your models here.

class Collaborator(models.Model):
    collaborator_name = models.CharField(max_length=200)
    collaborator_url = models.TextField()

    def __unicode__(self):
        return self.collaborator_name

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.category_name

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_dir_name = models.CharField(max_length=200)
    project_date = models.DateField()
    project_desc = models.TextField()
    project_url = models.TextField(null=True, blank=True)
    project_repo = models.TextField(null=True, blank=True)
    collaborators = models.ManyToManyField(Collaborator, null=True, blank=True)
    categories = models.ManyToManyField(Category, null=True, blank=True)

    def __unicode__(self):
        return self.project_name

class Media(models.Model):
    project = models.ForeignKey(Project)
    media_desc = models.TextField()
    media_url = models.TextField()

class Press(models.Model):
    project = models.ForeignKey(Project)
    press_desc = models.TextField()
    press_name = models.TextField()
    press_url = models.TextField()

    def __unicode__(self):
        return self.press_name + " - " + self.press_desc
