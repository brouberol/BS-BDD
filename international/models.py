# -*- coding: utf-8 -*-
"""
International instances : countries & faculties
"""

from django.db import models


class Pays(models.Model):
    """List of all countries"""
    nom = models.CharField(max_length=40)

    def __unicode__(self):
        return '%s' % self.nom
    
    class Meta:
        verbose_name_plural = u'Pays'

class Universite(models.Model):
    """Faculty situated abroad"""
    nom  = models.CharField(max_length=100, verbose_name=u"Nom de l'université")
    pays = models.ForeignKey(Pays)

    def __unicode__(self):
        return '%s - %s' %(self.nom, self.pays)

    class Meta:
        unique_together = [('nom', 'pays')]
        verbose_name = u"Université"
        verbose_name_plural = u"Universités"

        
