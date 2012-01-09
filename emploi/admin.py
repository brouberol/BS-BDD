"""
Admin interface tweaking for the emploi models
"""

from emploi.models import Emploi
from django.contrib import admin

class EmploiAdmin(admin.ModelAdmin):
    """Admin model of the FiliereAdmission model"""

    list_display = ('titre',)
    search_fields = ('titre',)
    list_filter = ['entreprise__domaine_general__nom',]

admin.site.register(Emploi, EmploiAdmin)

