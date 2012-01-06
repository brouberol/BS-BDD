"""
Admin interface tweaking for EtatCivil model
"""

from etat_civil.models import EtatCivil
from django.contrib import admin

class EtatCivilAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Informations administratives', {'fields': ['prenom', 'nom_insa', 'nom_actuel', 'sexe', 'date_naissance', 'nationalite', 'num_etudiant']}),
        ('Adresses'                    , {'fields': ['email_1', 'email_2', 'adresse_1', 'zip_adresse_1', 'adresse_2', 'zip_adresse_2']})
        ]
    list_display = ('prenom', 'nom_insa', 'sexe', 'num_etudiant', 'nationalite', 'email_1') 
    search_fields = ('prenom', 'nom_insa', 'nom_actuel', 'nationalite')
    list_filter = ['nationalite', 'sexe']

admin.site.register(EtatCivil, EtatCivilAdmin)
