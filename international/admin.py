# -*- coding: utf-8 -*-

"""
Admin registering for Univ model
"""

from international.models import Universite, Pays
from django.contrib import admin

admin.site.register(Universite)
admin.site.register(Pays)
