"""
Admin interface tweaking for the annee models
"""

from annee.models import AnneeBS, Echange, EchangeEleve
from django.contrib import admin

class AnneeBSAdmin(admin.ModelAdmin):
    """Admin registering of the AnneeBS model"""

    list_display = ('filiere','categorie', 'num_promo')
    list_filter = ['filiere','categorie']

admin.site.register(AnneeBS, AnneeBSAdmin)
admin.site.register(Echange)
admin.site.register(EchangeEleve)

