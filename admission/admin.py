"""
Admin registering for the preBS models
"""

from admission.models import Admission, FiliereAdmission, DomaineAdmission
from django.contrib import admin

class FiliereAdmissionAdmin(admin.ModelAdmin):
    """Admin model of the FiliereAdmission model"""
    search_fields = ('nom',)

class DomaineAdmissionAdmin(admin.ModelAdmin):
    """Admin model of the DomaineAdmission model"""
    search_fields = ('nom',)

class AdmissionAdmin(admin.ModelAdmin):
    """Admin model of the Admission model"""
    list_display = ('annee_admission', 'domaine_org', 'filiere_org',)
    list_filter = ['filiere_org__nom','annee_admission']

admin.site.register(FiliereAdmission, FiliereAdmissionAdmin)
admin.site.register(DomaineAdmission, DomaineAdmissionAdmin)
admin.site.register(Admission       , AdmissionAdmin       )
