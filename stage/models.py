# -*- coding: utf-8 -*-
"""
Models describing internships and their relation with students and scholar years
"""

from django.db import models
from django.template.defaultfilters import slugify

from emploi.models import Employeur
from annee.models import PromoBSEleve

class Stage(models.Model):
    """Model describing an internship"""
    
    employeur = models.ForeignKey(Employeur)
    sujet     = models.TextField(max_length=2000, blank=True)
    duree     = models.PositiveSmallIntegerField(help_text=u"En mois. Mettez un chiffre rond", verbose_name=u"Durée du stage", blank=True, null=True)
    salaire   = models.DecimalField(max_digits=6, decimal_places=2, help_text=u"En euros", blank=True, null=True)

    def __unicode__(self):
        return '%s - %s' % (self.employeur, slugify(self.sujet))

class StageEleve(models.Model):
    """Association between an internship and the scholar year of a student"""
    
    promo_eleve = models.ForeignKey(PromoBSEleve, unique=True)
    stage       = models.ForeignKey(Stage)

    def __unicode__(self):
        return '%s - %s' %(self.promo_eleve, self.stage)

    class Meta:
        verbose_name = u"Stage effectué par un élève"
        verbose_name_plural = u"Stages effectués par des élèves"
    
