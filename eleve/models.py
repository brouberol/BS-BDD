# -*- coding: utf-8 -*-
"""
Model defining the user and its groups & rights
"""

from django.db import models
from django.contrib.auth.models import User

from etat_civil.models import EtatCivil
from admission.models import Admission


class Eleve(models.Model):
    """
    An 'Eleve' is an authenticated user that can post and update
    data on the website.
    """
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #User model is defined in the django1.3.pdf doc, p226
    #Parameters:
    #username: 30char MAX, can contain @ + . - (REQUIRED)
    #first_name: 30 char MAX. (OPTIONAL)
    #last_name : 30 char MAX. (OPTIONAL)
    #email (OPTIONAL)
    #password: hash/metadata about password (REQUIRED)
    #is_staff: bool 
    #is_active: bool. DO NOT DELETE ACCOUNTS, put is_active=False
    #is_superuser: bool
    #last_login: auto
    #date_joined: auto
    etat_civil = models.OneToOneField(EtatCivil, on_delete=models.CASCADE)
    admission  = models.OneToOneField(Admission, on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s %s - %s - %d" %(self.etat_civil.prenom, self.etat_civil.nom_insa, self.user.username, self.etat_civil.num_etudiant) 

    class Meta:
        verbose_name = u"Élève"

