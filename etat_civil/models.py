# -*- coding: utf-8 -*-

"""
Administrative information about former students
"""

from django.db import models

class EtatCivil(models.Model):
    """
    Model defining the adminstrative information about a former student

    This model will be completed by the information stored in the Django standard
    User model : first/last name, email1, username, etc
    """

    SEXE_SELECTION = (
        ('H', 'H'),
        ('F', 'F'),
        )
       
    num_etudiant   = models.PositiveIntegerField(verbose_name=u"Numéro d'étudiant")
    sexe           = models.CharField(max_length=1, choices=SEXE_SELECTION, verbose_name=u"Sexe")
    nationalite    = models.CharField(max_length=30)
    date_naissance = models.DateField(verbose_name=u"Date de naissance")
    adresse_1      = models.TextField(max_length=200, verbose_name=u"Adresse personnelle", blank=True)
    zip_adresse_1  = models.PositiveIntegerField(blank=True)
    adresse_2      = models.TextField(max_length=200, verbose_name=u"Adresse familiale", blank=True)
    zip_adresse_2  = models.PositiveIntegerField(blank=True)
    email_2        = models.EmailField(blank=True)
    
