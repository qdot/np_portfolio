from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^np_portfolio/', include('np_portfolio.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^portfolio/$', 'np_portfolio.portfolio.views.index'),
    (r'^portfolio/(?P<project_name>[a-zA-Z0-9_-]+)$', 'np_portfolio.portfolio.views.project'),
    (r'^portfolio/(?P<project_name>[a-zA-Z0-9_-]+)/articles/(?P<article_name>[a-zA-Z0-9_-]+)$', 'np_portfolio.portfolio.views.article'),
)
