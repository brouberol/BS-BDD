# -*- coding: utf-8 -*-

"""
Admin interface registering for Stage & StageEleve model
"""

from stage.models import Stage, StageEleve
from django.contrib import admin

admin.site.register(Stage)
admin.site.register(StageEleve)
