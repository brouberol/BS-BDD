# -*- coding: utf-8 -*-

"""
Administrative information about former students
"""

from django.db import models

class EtatCivil(models.Model):
    """Model defining the adminstrative information about a former student"""

    SEXE = (('H', 'H'),('F', 'F'),)
       
    nom_insa       = models.CharField(max_length=30, verbose_name=u"Nom à l'INSA")
    nom_actuel     = models.CharField(max_length=30, verbose_name=u"Nom actuel", blank=True)
    prenom         = models.CharField(max_length=30, verbose_name=u"Prénom")
    num_etudiant   = models.PositiveIntegerField(verbose_name=u"Numéro d'étudiant", unique=True)
    sexe           = models.CharField(max_length=1, choices=SEXE, verbose_name=u"Sexe")
    date_naissance = models.DateField(verbose_name=u"Date de naissance", help_text=u"jj/mm/aaaa") # FIXME : nationalite devrait être un foreign key vers id pays !
    nationalite    = models.CharField(max_length=30, verbose_name=u"Nationalité")
    adresse_1      = models.TextField(max_length=200, verbose_name=u"Adresse personnelle", blank=True)
    zip_adresse_1  = models.PositiveIntegerField(verbose_name=u"Code postal de l'adresse personnel", null=True, blank=True)
    # blank = True different from null = True. If CharField/TextField = blank --> '' will be stored in DB
    # null = True implies that a NULL value can be stored in DB
    adresse_2      = models.TextField(max_length=200, verbose_name=u"Adresse familiale", blank=True)
    zip_adresse_2  = models.PositiveIntegerField(verbose_name=u"Code postal de l'adresse personnelle", null=True, blank=True)
    email_1        = models.EmailField(verbose_name=u"Email 1", blank=True)
    email_2        = models.EmailField(verbose_name=u"Email 2", blank=True)

    def __unicode__(self):
        """Determines how an 'etat civil' instance will be displayed """
        return u'{0} {1} - {2} - {3}'.format(self.prenom, self.nom_insa, self.sexe, self.num_etudiant)
    
    class Meta:
        verbose_name_plural = u"Etats civils"
