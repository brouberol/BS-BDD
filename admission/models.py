# -*- coding: utf-8 -*-
"""
Information about scholar cursus before attending BS
"""

from django.db import models

class FiliereAdmission(models.Model):
    """
    This model lists all possible 'filières' that a student
    could have studied in before BS
    """
    nom = models.CharField(max_length=50)

    def __unicode__(self):
        """Determines how a FiliereAdmission instance will be displayed"""
        return u'%s' % self.nom

    class Meta:
        verbose_name        = u"Filière d'origine"
        verbose_name_plural = u"Filières d'origine"

class DomaineAdmission(models.Model):
    """
    This model lists all possible domains that a student
    could have studied in before BS, being more precise than
    the FiliereAdmission model
    """
    nom = models.CharField(max_length=50)

    def __unicode__(self):
        """Determines how a DomaineAdmission instance will be displayed"""
        return u'%s' % self.nom

    class Meta:
        verbose_name        = u"Domaine d'origine"
        verbose_name_plural = u"Domaines d'origine"

class Admission(models.Model):
    """
    This model stores information about the scholar curus
    of a student before he/she attented BS
    """

    ANNEE_ADMISSION = (
        (3, '3'),
        (4, '4'),
        (5, '5'),
        )

    filiere_org         = models.OneToOneField(FiliereAdmission, on_delete=models.CASCADE, verbose_name=u"Filière d'origine")
    domaine_org         = models.OneToOneField(DomaineAdmission, on_delete=models.CASCADE, verbose_name=u"Domaine de la filière d'origine")
    annee_admission     = models.PositiveIntegerField(choices=ANNEE_ADMISSION, verbose_name=u"Année d'admission")
    rang_pre_BS         = models.PositiveIntegerField(verbose_name=u"Classement avant admission en BS", null=True)
    taille_promo_pre_BS = models.PositiveIntegerField(verbose_name=u"Taille de la promo avant admission en BS", null=True)

    def __unicode__(self):
        """Determines how an Admission instance will be displayed"""
        return u'%s - %s - %de année' %(self.filiere_org, self.domaine_org, self.annee_admission)
