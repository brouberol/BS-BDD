"""
Admin interface tweaking for the annee models
"""

from annee.models import AnneeBS
from django.contrib import admin

class AnneeBSAdmin(admin.ModelAdmin):
    """Admin model of the AnneeBS model"""

    list_display = ('filiere','categorie', 'num_promo')
    list_filter = ['filiere','categorie']

admin.site.register(AnneeBS, AnneeBSAdmin)

