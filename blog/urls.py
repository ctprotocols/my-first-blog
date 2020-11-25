# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 13:55:27 2020

@author: EastmanE
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]