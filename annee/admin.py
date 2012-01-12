"""
Admin registering the annee models
"""

from annee.models import PromoBS, PromoBSEleve, EchangeEleve, ResultatEleve
from django.contrib import admin

class PromoBSModelAdmin(admin.ModelAdmin):
    """Admin registering of the AnneeBS model"""
    list_display = ('niveau', 'filiere', 'categorie', 'num_promo')
    list_filter = ['filiere','categorie', 'niveau']

class PromoBSEleveModelAdmin(admin.ModelAdmin):
    list_display = ('eleve', 'promo_bs')
    list_filter = ['eleve__etat_civil__prenom', 'eleve__etat_civil__nom_insa']

class EchangeEleveModelAdmin(admin.ModelAdmin):
    list_display = ['promo_eleve','universite', 'duree']
    search_fields = ['promo_eleve__eleve__etat_civil__prenom', 'promo_eleve__eleve__etat_civil__nom_insa', 'universite__nom', 'universite__pays__nom']

class ResultatEleveModelAdmin(admin.ModelAdmin):
    list_display = ['promo_eleve','rang']
    search_fields = ['promo_eleve__eleve__etat_civil__prenom', 'promo_eleve__eleve__etat_civil__nom_insa']

admin.site.register(PromoBS, PromoBSModelAdmin)
admin.site.register(PromoBSEleve, PromoBSEleveModelAdmin)
admin.site.register(EchangeEleve, EchangeEleveModelAdmin)
admin.site.register(ResultatEleve, ResultatEleveModelAdmin)

