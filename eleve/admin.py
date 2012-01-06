# -*- coding: utf-8 -*-

"""
Admin interface tweaking for Eleve model
"""

from eleve.models import Eleve
from django.contrib import admin

#class EleveAdmin(admin.ModelAdmin):




    # user = models.OneToOneField(User)
    # #User model is defined in the django1.3.pdf doc, p226
    # #Parameters:
    # #username: 30char MAX, can contain @ + . - (REQUIRED)
    # #first_name: 30 char MAX. (OPTIONAL)
    # #last_name : 30 char MAX. (OPTIONAL)
    # #email (OPTIONAL)
    # #password: hash/metadata about password (REQUIRED)
    # #is_staff: bool 
    # #is_active: bool. DO NOT DELETE ACCOUNTS, put is_active=False
    # #is_superuser: bool
    # #last_login: auto
    # #date_joined: auto
    # etat_civil = models.OneToOneField(EtatCivil)
    # admission = models.OneToOneField(Admission)


    # readonly_fields = ('created_at', 'updated_at', 'sales',)
    # fieldsets = [
    #     ('Seller', {'fields': ['seller','departement', 'city']}),
    #     ('Description', {'fields': ['price','title', 'slug', 'categories', 'short_desc', 'long_desc', 'image', 'status']}),
    #     ('Miscellaneous', {'fields': ['created_at', 'updated_at', 'end_at', 'sales']}),
    #     ]
    # list_display = ('title', 'price', 'short_desc', 'seller', 'departement', 'status')
    # search_fields = ['title', 'short_desc','region','seller__last_name','seller__first_name']
    # date_hierarchy = 'created_at'
    # list_filter = ['categories__title']
    # filter_horizontal = ('categories',)
    # prepopulated_fields = {"slug": ("title",)}


admin.site.register(Eleve)#, EleveAdmin)
