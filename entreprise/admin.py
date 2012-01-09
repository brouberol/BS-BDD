"""
Admin interface tweaking for the entreprise models
"""

from entreprise.models import Entreprise, EntrepriseDomaineSpecifique, EntrepriseDomaineGeneral
from django.contrib import admin

class EntrepriseAdmin(admin.ModelAdmin):
    """Admin model of the FiliereAdmission model"""

    list_display = ('nom',)#, 'domaine_general__nom', 'domaine_specifique__nom')
    search_fields = ('nom',)
    #list_filter = ['nationalite', 'sexe']


class EntrepriseDomaineSpecifiqueAdmin(admin.ModelAdmin):
    """Admin model of the EntrepriseDomaineSpecifique model"""
    search_fields = ('nom',)

class EntrepriseDomaineGeneralAdmin(admin.ModelAdmin):
    """Admin model of the EntrepriseDomaineGeneral model"""
    search_fields = ('nom',)

admin.site.register(EntrepriseDomaineSpecifique, EntrepriseDomaineSpecifiqueAdmin)
admin.site.register(EntrepriseDomaineGeneral   , EntrepriseDomaineGeneralAdmin)
admin.site.register(Entreprise                 , EntrepriseAdmin)
