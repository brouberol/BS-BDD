# -*- coding: utf-8 -*-

"""
Admin interface registering for Stage & StageEleve model
"""

from stage.models import Stage, StageEleve
from django.contrib import admin

class StageEleveModelAdmin(admin.ModelAdmin):
    list_display = ('promo_eleve', 'stage')
    list_filter = ['promo_eleve']
    search_fields = ['stage__description', 'stage__employeur__nom', 'promo_eleve__eleve__etat_civil__nom_insa','promo_eleve__eleve__etat_civil__prenom']
    

admin.site.register(Stage)
admin.site.register(StageEleve)
