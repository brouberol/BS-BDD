"""
Test suite for the Admission application.
"""

from django.utils import unittest
from django.test import TestCase, TransactionTestCase
from django.core.exceptions import ObjectDoesNotExist

from admission.models import Admission, FiliereAdmission, DomaineAdmission

class FiliereAdmissionModelUnitTest(TestCase):
    
    def test_create_filiere_admission(self):
        fa = FiliereAdmission(nom='Ecole Jedi')
        fa.save()

        # fa exists in DB ?
        self.assertNotEqual(fa.id, 0)

         # can we retrieve fa in DB ?
        fa_id = fa.id     
        fa = None
        fa = FiliereAdmission.objects.get(nom='Ecole Jedi')
        self.assertEqual(fa.id, fa_id)

class DomaineAdmissionModelUnitTest(TestCase):
    
    def test_create_domaine_admission(self):
        da = DomaineAdmission(nom='Parachutage')
        da.save()
        
        # da exists in DB ?
        self.assertNotEqual(da.id, 0)

        # can we retrieve da in DB ?
        da_id = da.id     
        da = None
        da = DomaineAdmission.objects.get(nom='Parachutage')
        self.assertEqual(da.id, da_id)
        
class AdmissionModelUnitTest(TestCase):

    def setUp(self):
        fa = FiliereAdmission(nom='Ecole Jedi')
        da = DomaineAdmission(nom='Parachutage')
        fa.save()
        da.save()

    def test_create_admission(self):
        fa = FiliereAdmission.objects.get(nom='Ecole Jedi')
        da = DomaineAdmission.objects.get(nom='Parachutage')

        ad = Admission()
        ad.filiere_org = fa
        ad.domaine_org = da
        ad.annee_admission = 3
        ad.rang_pre_BS = 5
        ad.taille_promo_pre_BS = 100
        ad.save()

        # ad exists in DB ?
        self.assertNotEqual(ad.id, 0)
        
        # can we retrieve ad in DB ?
        ad_id = ad.id     
        ad = None
        ad = Admission.objects.get(id = ad_id)
        self.assertEqual(ad.filiere_org, fa)
        self.assertEqual(ad.domaine_org, da)
        self.assertEqual(ad.annee_admission, 3)
        self.assertEqual(ad.rang_pre_BS, 5)
        self.assertEqual(ad.taille_promo_pre_BS, 100)
