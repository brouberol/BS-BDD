"""
Test suite for the EtatCivil application.
"""

import datetime

from django.utils import unittest
from django.test import TestCase, TransactionTestCase
from django.core.exceptions import ObjectDoesNotExist

from etat_civil.models import EtatCivil

class EtatCivilModelUnitTest(TestCase):

    def setUp(self):
        ec = EtatCivil(nom_insa='Test')
        ec.nom_actuel = 'Test'
        ec.prenom = "Test"
        ec.num_etudiant = '26760'
        ec.sexe = 'F'
        ec.date_naissance = datetime.date(1960, 11, 4)
        ec.nationalite = 'Fr'
        ec.adresse_1 = 'adresse test 1'
        ec.zip_adresse_1 = '21897'
        ec.adresse_2 = 'adresse test 2'
        ec.zip_adresse_2 = '60410'
        ec.email_1 = 'email test 1'
        ec.email_2 = 'email test 2'
        ec.save()


    def test_create_etat_civil(self):
        """ Save/Get testing """
        ec = EtatCivil(nom_insa='Bidochon')
        ec.nom_actuel = 'Galopin'
        ec.prenom = "Raymonde"
        ec.num_etudiant = '2676'
        ec.sexe = 'F'
        ec.date_naissance = datetime.date(1967, 11, 4)
        ec.nationalite = 'Fr'
        ec.adresse_1 = '2 rue de la bidoche'
        ec.zip_adresse_1 = '21897'
        ec.adresse_2 = '4 rue de la tranche de mortadelle'
        ec.zip_adresse_2 = '60410'
        ec.email_1 = 'c_est_quoi_un_email@wanadoo.fr'
        ec.email_2 = 'a@pe.ro'
        ec.save()

        # ec exists in DB ?
        self.assertNotEqual(ec.id, 0)

        # can we retrieve ec in DB ?
        ec_id = ec.id     
        ec = None
        ec = EtatCivil.objects.get(nom_insa = 'Bidochon')
        self.assertEqual(ec.id, ec_id)
        self.assertEqual(ec.nom_actuel, 'Galopin')
        self.assertEqual(ec.prenom, 'Raymonde')
        self.assertEqual(ec.num_etudiant, long(2676))
        self.assertEqual(ec.sexe, 'F')
        self.assertEqual(ec.date_naissance, datetime.date(1967, 11, 4))
        self.assertEqual(ec.nationalite, 'Fr')
        self.assertEqual(ec.adresse_1, '2 rue de la bidoche')
        self.assertEqual(ec.zip_adresse_1, long(21897))
        self.assertEqual(ec.adresse_2, '4 rue de la tranche de mortadelle')
        self.assertEqual(ec.zip_adresse_2, long(60410))
        self.assertEqual(ec.email_1, 'c_est_quoi_un_email@wanadoo.fr')
        self.assertEqual(ec.email_2, 'a@pe.ro')

        
        
