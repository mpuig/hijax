# -*- coding: utf-8 -*-
"""
    hijax.app
    ~~~~~~~~~

    This demo is a proof of concept for the hijax technique, with Django
    Based on the example found at http://duganchen.ca/single-page-web-app-architecture-done-right
    More about Hijax: http://en.wikipedia.org/wiki/Hijax
    
    :autor: 2011 by Marc Puig (marc.puig@gmail.com).
"""

import pystache
 
class Items(pystache.View):
    def set_items(self, items):
        self.__items = items
    def items(self):
        return self.__items
 
class Edit(pystache.View):
    def set_item(self, item):
        self.__item = item
    def item(self):
        return self.__item
 
class Outline(pystache.View):
    def set_body(self, body):
        self.__body = body
    def body(self):
        return self.__body.render()