# -*- coding: utf-8 -*-
"""
URLs related to data upload
"""

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'upload.views.upload', name='input'),
)
