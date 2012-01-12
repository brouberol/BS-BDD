"""
Admin interface tweaking for the emploi models
"""

from emploi.models import Emploi, Employeur, EmployeurDomaineSpecifique, EmployeurDomaineGeneral, Position, EmploiEleve, Situation
from django.contrib import admin

class EmploiAdmin(admin.ModelAdmin):
    """Admin model of the FiliereAdmission model"""

    list_display = ('description',)
    search_fields = ('description',)
    list_filter = ['employeur__domaine_general__nom',]

admin.site.register(Emploi, EmploiAdmin)
admin.site.register(Employeur)
admin.site.register(EmployeurDomaineGeneral)
admin.site.register(EmployeurDomaineSpecifique)
admin.site.register(Position)
admin.site.register(Situation)
admin.site.register(EmploiEleve)

