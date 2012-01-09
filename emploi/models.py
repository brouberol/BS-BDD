# -*- coding: utf-8 -*-
"""
Model describing job titles chosen by former student
"""

from django.db import models

from entreprise.models import Entreprise

class Emploi(models.Model):
    """Job title description"""
    
    titre      = models.CharField(max_length=75, verbose_name=u'Description du poste')
    entreprise = models.ForeignKey(Entreprise)
    
