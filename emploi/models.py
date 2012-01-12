# -*- coding: utf-8 -*-
"""
Model describing job titles chosen by former student, and companies
"""

from django.db import models

class EmployeurDomaineSpecifique(models.Model):
    """Specific company domain description"""
    nom = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        """ EmployeurDomaineSpecifique representation"""
        return '%s' %(self.nom)

    class Meta:
        verbose_name = u"Domaine spécifique de l'entreprise"
        verbose_name_plural = u"Domaines spécifiques de l'entreprise"
        ordering = ['nom']

class EmployeurDomaineGeneral(models.Model):
    """General company domain description"""
    nom = models.CharField(max_length=50, unique=True)
    
    def __unicode__(self):
         """ EmployeurDomaineGeneral representation"""
         return '%s' %(self.nom)

    class Meta:
        verbose_name = u"Domaine général de l'entreprise"
        verbose_name_plural = u"Domaines généraux de l'entreprise"
        ordering = ['nom']
        
class Employeur(models.Model):
    """Company/university description"""
    
    TAILLE = ( # SPECIFIC TABLE ?
        ('<20', '<20'),
        ('20-250', '20-250'),
        ('250-500', '250-500'),
        ('500-2000', '500-2000'),
        ('>2000', '>2000'),
        )

    nom                = models.CharField(max_length=50)
    adresse            = models.TextField(max_length=150, blank=True)
    zip_adresse        = models.PositiveIntegerField(verbose_name=u"Code postal", null=True, blank=True)
    taille             = models.CharField(max_length=20, choices=TAILLE, blank=True)
    domaine_general    = models.ManyToManyField(EmployeurDomaineGeneral, null=True)
    domaine_specifique = models.ManyToManyField(EmployeurDomaineSpecifique, null=True)
    
    def __unicode__(self):
        """Employeur instance representation"""
        return '%s' %(self.nom)

class Position(models.Model):
    """Type of jobs, defined by the Levy table """
    nom = models.CharField(max_length=50)

class Emploi(models.Model):
    """Job title description"""

    entreprise  = models.ManyToManyField(Employeur)
    description = models.CharField(max_length=75, verbose_name=u'Description du poste')
    position    = models.ForeignKey(Position)
   
