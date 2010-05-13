from np_portfolio.portfolio import models
from django.contrib.contenttypes import generic
from django.contrib import admin

class PhotoInline(admin.TabularInline):
    model = models.Photo
    extra = 1

class MediaInline(admin.TabularInline):
    model = models.Media.projects.through
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, MediaInline]

admin.site.register(models.Collaborator)
admin.site.register(models.Category)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Media)
admin.site.register(models.Press)
admin.site.register(models.Photo)
admin.site.register(models.MediaType)

