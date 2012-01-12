# -*- coding: utf-8 -*-
"""
Model defining different types of scholar year
"""

from django.db import models

from BS.eleve.models import Eleve
from BS.international.models import Universite

class AnneeBS(models.Model):
    """A traditional BS scholar year"""
    
    FILIERE = (
        ('BIM', 'BIM'),
        ('BB', 'BB'),
        ('Bioch', 'Bioch'),
        )

    CATEGORIE = (('3','3'), ('4','4'), ('5','5'), ('Cesure', 'Césure'), ('Sabbatique', 'Sabbatique'), ('Echange', 'Échange académique'))
        
    categorie    = models.CharField(max_length=10, choices=CATEGORIE, verbose_name=u"Type d'année")
    filiere      = models.CharField(max_length=5, choices=FILIERE, verbose_name=u'Filière', help_text=u"Bioch : filière avant 199X") # TODO : update help_text
    num_promo    = models.PositiveIntegerField(verbose_name=u'Numéro de la promotion')
    taille_promo = models.PositiveIntegerField(verbose_name=u'Taille de la promotion')
    annee        = models.PositiveIntegerField(help_text=u"Indiquer l'année de début de l'année scolaire (ex: 2011 pour 2011-2012)")

    def __unicode__(self):
        """ AnneeBS instance representation """
        if self.categorie not in ['3', '4', '5']: # cesure / sabbatique
            return '%s - %s - %d - Promo %d' %(self.filiere, self.categorie, self.annee, self.num_promo)
        else:
            return '%s%s - %d - Promo %d' %(self.categorie, self.filiere, self.annee, self.num_promo)

    class Meta:
        verbose_name = u"Année de scolarité BS"
        verbose_name_plural = u"Années de scolarité BS"
        unique_together = [('categorie', 'filiere', 'num_promo')]

class AnneeBSEleve(models.Model):
    """Association between a student and a BS scholar year"""
    
    eleve    = models.ForeignKey(Eleve)
    annee_bs = models.ForeignKey(AnneeBS)


class EchangeEleve(models.Model):
    """Association between an academic exchange and a student's scholar year"""
    
    universite  = models.ForeignKey(Universite, verbose_name=u"Université d'accueil")
    annee_eleve = models.ForeignKey(AnneeBSEleve, verbose_name=u"Année d'échange") 
    duree       = models.PositiveSmallIntegerField(verbose_name=u"Durée de l'échange", help_text=u"En mois. Donnez un nombre rond.")

    def __unicode__(self):
        return '%s - %s - %s - %d mois' %(self.annee_eleve, self.universite.pays, self.universite.nom, self.duree)

    class Meta:
        verbose_name =u"Élève parti en échange académique"
        verbose_name_plural = u"Élèves partis en échange académique"


class ResultatEleve(models.Model):
    """Association between a student's scholar year and his/her results"""

    annee_eleve = models.ForeignKey(AnneeBSEleve, verbose_name=u"Élève & année scolaire")
    rang        = models.PositiveIntegerField(verbose_name=u"Classement")
   
