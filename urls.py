# -*- coding: utf-8 -*-
"""
    hijax.app
    ~~~~~~~~~

    This demo is a proof of concept for the hijax technique, with Django
    Based on the example found at http://duganchen.ca/single-page-web-app-architecture-done-right
    More about Hijax: http://en.wikipedia.org/wiki/Hijax
    
    :autor: 2011 by Marc Puig (marc.puig@gmail.com).
"""

from django.conf.urls.defaults import patterns, include, url
from django.views.generic import RedirectView
from django.conf import settings

urlpatterns = patterns('',
    ('^$', RedirectView.as_view(url='/items')),
    ('^items$', 'items.views.items'),
    ('^edit/1$', 'items.views.edit'),
    ('^ajax/items$', 'items.views.items_ajax'),
    ('^ajax/edit$', 'items.views.edit_ajax'),
)

if settings.DEBUG:
    urlpatterns+= patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_items': True})
    )
