# -*- coding: utf-8 -*-
"""
Information about companies
"""

from django.db import models

class EntrepriseDomaineSpecifique(models.Model):
    """Specific company domain description"""
    nom = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        """ EntrepriseDomaineSpecifique representation"""
        return '%s' %(self.nom)

    class Meta:
        verbose_name = u"Domaine spécifique de l'entreprise"
        verbose_name_plural = u"Domaines spécifiques de l'entreprise"
        ordering = ['nom']

class EntrepriseDomaineGeneral(models.Model):
    """General company domain description"""
    nom = models.CharField(max_length=50, unique=True)
    
    def __unicode__(self):
         """ EntrepriseDomaineGeneral representation"""
         return '%s' %(self.nom)

    class Meta:
        verbose_name = u"Domaine général de l'entreprise"
        verbose_name_plural = u"Domaines généraux de l'entreprise"
        ordering = ['nom']
        
class Entreprise(models.Model):
    """Company description"""
    
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
    domaine_general    = models.ManyToManyField(EntrepriseDomaineGeneral, null=True)
    domaine_specifique = models.ManyToManyField(EntrepriseDomaineSpecifique, null=True)
    
    def __unicode__(self):
        """Entreprise instance representation"""
        return '%s' %(self.nom)
