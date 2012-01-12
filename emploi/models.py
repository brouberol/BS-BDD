# -*- coding: utf-8 -*-
"""
Model describing job titles chosen by former student, and companies
"""

from django.db import models

from eleve.models import Eleve

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
    adresse            = models.CharField(max_length=150, blank=True)
    zip_adresse        = models.PositiveIntegerField(verbose_name=u"Code postal", null=True, blank=True)
    taille             = models.CharField(max_length=20, choices=TAILLE, blank=True)
    domaine_general    = models.ManyToManyField(EmployeurDomaineGeneral, null=True)
    domaine_specifique = models.ManyToManyField(EmployeurDomaineSpecifique, null=True)
    
    def __unicode__(self):
        """Employeur instance representation"""
        return '%s' %(self.nom)

class Position(models.Model):
    """Type of jobs, defined by the Levy table """
    nom = models.CharField(max_length=50, unique=True)
    
    def __unicode__(self):
        return "%s" % self.nom
    
    class Meta:
        ordering= ['nom']
        
class Emploi(models.Model):
    """Job title description"""
    
    employeur  = models.ForeignKey(Employeur)
    description = models.CharField(max_length=75, verbose_name=u'Description du poste')
    
    def __unicode__(self):
        return '%s - %s' %(self.employeur.nom, self.description)

class Situation(models.Model):
    """Model describing the state of employement of a person"""
    nom = models.CharField(max_length=30)

    def __unicode__(self):
        return '%s' % self.nom
    
class EmploiEleve(models.Model):
    """Association between a former student and a job position"""
    
    eleve           = models.ForeignKey(Eleve)
    emploi          = models.ForeignKey(Emploi, null=True)
    situation       = models.ForeignKey(Situation)
    position        = models.ForeignKey(Position, null=True)
    annee           = models.PositiveIntegerField(verbose_name=u"Année d'embauche", null=True)
    salaire         = models.PositiveIntegerField(null=True)
    duree_recherche = models.PositiveIntegerField(verbose_name=u"Durée de recherche d'emploi", help_text=u"En mois. Mettez un chiffre rond", null=True)
  
    def __unicode__(self):
        return '%s %s - %s' %(self.eleve.etat_civil.prenom, self.eleve.etat_civil.nom_insa, self.emploi)

    class Meta:
        verbose_name =u"Élève employé"
        verbose_name_plural = u"Élèves employés"
        unique_together = [('eleve', 'emploi', 'position', 'annee')]
     
     
