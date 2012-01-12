"""
Admin registering for the emploi models
"""

from emploi.models import Emploi, Employeur, EmployeurDomaineSpecifique, EmployeurDomaineGeneral, Position, EmploiEleve, Situation, DifficulteRecherche
from django.contrib import admin

class EmploiModelAdmin(admin.ModelAdmin):
    """Admin model of the FiliereAdmission model"""
    list_display = ('description',)
    search_fields = ('description',)
    list_filter = ['employeur__domaine_general__nom',]

class EmployeurModelAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom', 'adresse', 'zip_adresse']
    list_filter = ['nom', 'domaine_general__nom']

class EmploiEleveModelAdmin(admin.ModelAdmin):
    list_display = ('eleve', 'situation', 'emploi', 'position')
    search_fields = ['eleve__etat_civil__nom_insa', 'eleve__etat_civil__prenom', 'emploi__description', 'emploi__employeur__nom']

admin.site.register(Emploi, EmploiModelAdmin)
admin.site.register(Employeur, EmployeurModelAdmin)
admin.site.register(EmployeurDomaineGeneral)
admin.site.register(EmployeurDomaineSpecifique)
admin.site.register(Position)
admin.site.register(Situation)
admin.site.register(EmploiEleve, EmploiEleveModelAdmin)
admin.site.register(DifficulteRecherche)

