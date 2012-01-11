# -*- coding: utf-8 -*-
"""
Model defining different types of scholar year
"""

from django.db import models
from univ.models import Universite

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
    # TODO ; add date  (20XX - 20XX)

    def __unicode__(self):
        """ AnneeBS instance representation """
        if self.categorie not in ['3', '4', '5']: # cesure / sabbatique
            return '%s - %s - Promo %d' %(self.filiere, self.categorie, self.num_promo)
        else:
            return '%s%s - Promo %d' %(self.categorie, self.filiere, self.num_promo)

    class Meta:
        verbose_name = u"Année de scolarité BS"
        verbose_name_plural = u"Années de scolarité BS"
        unique_together = [('categorie', 'filiere', 'num_promo')]

class Echange(models.Model):
    """Academic exchange"""
    
    universite = models.ForeignKey(Universite, verbose_name=u"Université d'accueil")
    duree      = models.PositiveSmallIntegerField(verbose_name=u"Durée de l'échange", help_text=u"En mois. Donnez un nombre rond.")

    def __unicode__(self):
        return '%s - %s - %d mois' %(self.universite.pays, self.universite.nom, self.duree)
    

class EchangeEleve(models.Model):
    """Instance of the relation student <-> academic exchange"""
    
    from eleve.models import Eleve
    
    eleve    = models.ForeignKey(Eleve)
    annee_bs = models.ForeignKey(AnneeBS)
    echange  = models.ForeignKey(Echange)
    
    def __unicode__(self):
        return '%s - %s' %(self.annee_bs, self.echange)
    
    class Meta:
        verbose_name =u"Élève parti en échange académique"
        verbose_name_plural = u"Élèves partis en échange académique"


