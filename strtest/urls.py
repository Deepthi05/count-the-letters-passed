"""
URLs for the strtest app.
"""
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'strex_prathibha.views.teststr', name='strtest'),
)
