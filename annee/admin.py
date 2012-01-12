"""
Admin registering the annee models
"""

from annee.models import PromoBS, PromoBSEleve, EchangeEleve, ResultatEleve
from django.contrib import admin

class PromoBSAdmin(admin.ModelAdmin):
    """Admin registering of the AnneeBS model"""
    list_display = ('niveau', 'filiere', 'categorie', 'num_promo')
    list_filter = ['filiere','categorie', 'niveau']

admin.site.register(PromoBS, PromoBSAdmin)
admin.site.register(PromoBSEleve)
admin.site.register(EchangeEleve)
admin.site.register(ResultatEleve)

