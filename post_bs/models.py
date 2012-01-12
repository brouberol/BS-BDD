# -*- coding: utf-8 -*-
"""
Model describing post-BS studies
"""

from django.db import models

from eleve.models import Eleve
from emploi.models import EmployeurDomaineGeneral

class FormationPostBS(models.Model):
    
    nom = models.CharField(max_length=50, unique=True)
    
    def __unicode__(self):
        return '%s' %(self.nom)

    class Meta:
        verbose_name = u"Formation post-BS"
        verbose_name_plural = u"Formations post-BS"


class FormationPostBSEleve(models.Model):
    
    eleve     = models.ForeignKey(Eleve)
    formation = models.ForeignKey(FormationPostBS, null=True)
    domaine   = models.ForeignKey(EmployeurDomaineGeneral, null=True, blank=True)
    duree     = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Durée de la formation")

    def __unicode__(self):
        return '%s' %(self.eleve)

    class Meta:
        verbose_name = u"Élève ayant suivi une formation post-BS"
        verbose_name_plural = u"Élèves ayant suivi une formation post-BS"
        unique_together = ['eleve','formation','domaine']
        
