# -*- coding: utf-8 -*-

"""
Admin interface registering for Stage & StageEleve model
"""

from stage.models import Stage, StageEleve
from django.contrib import admin

class StageModelAdmin(admin.ModelAdmin):
    list_display = ('employeur', 'sujet')
    list_filter  = ['employeur__nom']
    search_fields = ['employeur__nom', 'sujet']

class StageEleveModelAdmin(admin.ModelAdmin):
    list_display = ('promo_eleve', 'stage')
    list_filter = ['promo_eleve__promo_bs']
    search_fields = ['stage__sujet', 'stage__employeur__nom', 'promo_eleve__eleve__etat_civil__nom_insa','promo_eleve__eleve__etat_civil__prenom']
    

admin.site.register(Stage, StageModelAdmin)
admin.site.register(StageEleve, StageEleveModelAdmin)
