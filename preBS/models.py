# -*- coding: utf-8 -*-
"""
Information about scholar cursus before attending BS
"""

from django.db import models

class FilierePreBS(models.Model):
    """
    This model lists all possible 'filières' that a student
    could have studied in before BS
    """
    nom = models.CharField(max_length=50)

class DomainePreBS(models.Model):
    """
    This model lists all possible domains that a student
    could have studied in before BS, being more precise than
    the FilierePreBS model
    """
    nom = models.CharField(max_length=50)


class PreBS(models.Model):
    """
    This model stores information about the scholar curus
    of a student before he/she attented BS
    """

    ANNEE_ADMISSION = (
        (3, '3'),
        (4, '4'),
        (5, '5'),
        )

    filiere_org         = models.OneToOneField(FilierePreBS, on_delete=models.CASCADE)
    domaine_org         = models.OneToOneField(DomainePreBS, on_delete=models.CASCADE)
    annee_admission     = models.PositiveIntegerField(choices=ANNEE_ADMISSION)
    rang_pre_BS         = models.PositiveIntegerField(blank=True)
    taille_promo_pre_BS = models.PositiveIntegerField(blank=True)
