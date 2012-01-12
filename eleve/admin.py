# -*- coding: utf-8 -*-

"""
Admin interface tweaking for Eleve model
"""

from eleve.models import Eleve, EleveDiplome
from django.contrib import admin

admin.site.register(Eleve)
admin.site.register(EleveDiplome)
