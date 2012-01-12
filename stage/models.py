"""
Models describing internships and their relation with students and scholar years
"""

from django.db import models

from emploi.models import Employeur
from annee.models import AnneeBSEleve

class Stage(models.Model):
    """Model describing an internship"""
    
    employeur = models.ForeignKey(Employeur)
    sujet     = models.TextField(max_length=2000)
    duree     = models.PositiveSmallIntegerField(help_text=u"En mois. Mettez un chiffre rond", verbose_name=u"Durée du stage")
    salaire   = models.DecimalField(decimal_places=2)

class StageEleve(models.Model):
    """Association between an internship and the scholar year of a student"""
    
    annee_eleve = models.ForeignKey(AnneeBSEleve)
    stage       = models.ForeignKey(Stage)

    class Meta:
        verbose_name = u"Stage effectué par un élève"
        verbose_name_plural = u"Stages effectués par des élèves"
    
