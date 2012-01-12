# -*- coding: utf-8 -*-
"""
Model defining different types of scholar year
"""

from django.db import models

from BS.eleve.models import Eleve
from BS.international.models import Universite

class PromoBS(models.Model):
    """A traditional BS scholar year"""
    
    FILIERE = (
        ('BIM', 'BIM'),
        ('BB', 'BB'),
        ('Bioch', 'Bioch'),
        )

    ANNEE = (('3','3'), ('4','4'), ('5','5'))
    CATEGORIE =  (('Normale', 'Normale'), ('Cesure', 'Césure'), ('Sabbatique', 'Sabbatique'), ('Echange', 'Échange académique'))
    
    # WARNING : un echange ne peut pas etre associe a une annee de type 3/4/5/C/S

    # TODO (?) 2 attributs au lieu d'un seul (CATEGORIE):
    #  - annee : 3,4,5
    #  - type  : Normal, Echange, Sabbatique, Cesure
    
    niveau       = models.CharField(max_length=20, choices=ANNEE, verbose_name=u"Niveau de formation")
    filiere      = models.CharField(max_length=5, choices=FILIERE, verbose_name=u'Filière', help_text=u"Bioch : filière avant 199X") # TODO : update help_text
    categorie    = models.CharField(max_length=10, choices=CATEGORIE, verbose_name=u"Type d'année")
    num_promo    = models.PositiveIntegerField(verbose_name=u'Promotion', help_text=u'Indiquer la date de sortie')
    taille_promo = models.PositiveIntegerField(verbose_name=u'Taille de la promotion')
    annee        = models.PositiveIntegerField(help_text=u"Indiquer l'année de début de l'année scolaire (ex: 2011 pour 2011-2012)")

    def __unicode__(self):
        """ PromoBS instance representation """
        if self.categorie == 'Normale': 
            return '%s%s  - %d - Promo %d' %(self.niveau, self.filiere, self.annee, self.num_promo)
        else:
            return '%s%s - %s - %d - Promo %d' %(self.niveau, self.filiere, self.categorie,  self.annee, self.num_promo)

    class Meta:
        verbose_name = u"Promotion BS"
        verbose_name_plural = u"Promotions BS"
        unique_together = [('niveau', 'filiere','categorie', 'num_promo')]

class PromoBSEleve(models.Model):
    """Association between a student and a BS promotion"""
    
    eleve    = models.ForeignKey(Eleve)
    promo_bs = models.ForeignKey(PromoBS)

    def __unicode__(self):
        return '%s %s - %s%s - Promo %d' %(self.eleve.etat_civil.prenom, 
                                           self.eleve.etat_civil.nom_insa, 
                                           self.promo_bs.niveau, 
                                           self.promo_bs.filiere, 
                                           self.promo_bs.num_promo)

    class Meta:
        verbose_name = U"Élève par promotion"
        verbose_name_plural = u"Élèves par promotion"
        unique_together = [('eleve','promo_bs')]


class EchangeEleve(models.Model):
    """Association between an academic exchange and a student's scholar year"""
    
    universite  = models.ForeignKey(Universite, verbose_name=u"Université d'accueil")
    promo_eleve = models.ForeignKey(PromoBSEleve, verbose_name=u"Année d'échange", unique=True) 
    duree       = models.PositiveSmallIntegerField(verbose_name=u"Durée de l'échange", help_text=u"En mois. Donnez un nombre rond.")

    def __unicode__(self):
        return '%s - %s - %s - %d mois' %(self.promo_eleve, self.universite.pays, self.universite.nom, self.duree)

    class Meta:
        verbose_name =u"Élève parti en échange académique"
        verbose_name_plural = u"Élèves partis en échange académique"


class ResultatEleve(models.Model):
    """Association between a student's scholar year and his/her results"""

    # WARNING : no rank in 5th year

    promo_eleve = models.ForeignKey(PromoBSEleve, verbose_name=u"Élève & promotion")
    rang        = models.PositiveIntegerField(verbose_name=u"Classement")

    def __unicode__(self):
        return '%s - %d/%d' %(self.promo_eleve, self.rang, self.promo_eleve.promo_bs.taille_promo)
   
    class Meta:
        verbose_name = u"Résultat académique d'un élève"
        verbose_name_plural = "Résultats académiques des élèves"
