# -*- coding: utf-8 -*-
"""
URLs related to data upload
"""

from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', 'upload.views.upload', name='input'),
    url(r'^success/$', TemplateView.as_view(template_name="upload/success.html"))                
)
