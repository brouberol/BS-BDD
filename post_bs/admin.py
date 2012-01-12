# -*- coding: utf-8 -*-
"""
Admin registering the post_bs models
"""

from post_bs.models import FormationPostBS, FormationPostBSEleve
from django.contrib import admin



class FormationPostBSEleveModelAdmin(admin.ModelAdmin):
    """Admin registering of the FormationPostxAnneeBS model"""
    list_display = ('eleve', 'formation', 'domaine', 'duree')
    list_filter = ['eleve','formation', 'domaine']


admin.site.register(FormationPostBSEleve, FormationPostBSEleveModelAdmin)
admin.site.register(FormationPostBS)
