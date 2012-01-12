# -*- coding: utf-8 -*-

"""
Admin interface tweaking for Univ model
"""

from univ.models import Universite, Pays
from django.contrib import admin

admin.site.register(Universite)
admin.site.register(Pays)
