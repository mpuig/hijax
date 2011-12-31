# -*- coding: utf-8 -*-
"""
    hijax.app
    ~~~~~~~~~

    This demo is a proof of concept for the hijax technique, with Django
    Based on the example found at http://duganchen.ca/single-page-web-app-architecture-done-right
    More about Hijax: http://en.wikipedia.org/wiki/Hijax
    
    :autor: 2011 by Marc Puig (marc.puig@gmail.com).
"""

from django import http
import pystache
from items.templates import Outline, Items, Edit
import os

pystache.View.template_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates')
 
def items(request):
    """
    This is the "default" request, to show a list of items
    """
    outline_template = Outline()
    items_template = Items()
    items_template.set_items([{
        'id': '1',
        'item': 'Joe',
        },
        {
            'id': '2',
            'item': 'Victoria',
        }
    ])
    outline_template.set_body(items_template)
    return http.HttpResponse(outline_template.render())
 
def edit(request):
    """
    This is a "default" request, to show an edit form for an item.
    """
    outline_template = Outline()
    edit_template = Edit()
    edit_template.set_item('Joe')
    outline_template.set_body(edit_template)
    return http.HttpResponse(outline_template.render())
 
def items_ajax(request):
    """
    This is the "hijaxed" request, to show a list of items
    """
    
    items_template = Items()
    items_template.set_items([{
            'id': '1',
            'item': 'Joe',
        },
        {
            'id': '2',
            'item': 'Victoria',
        }
    ])
    return http.HttpResponse(items_template.render())
 
def edit_ajax(request):
    """
    This is the "hijaxed" request, to show an edit form for an item.
    """
    edit_template = Edit()
    edit_template.set_item('Joe')
    return http.HttpResponse(edit_template.render())