# -*- coding: utf-8 -*-
"""
Views related to data input
"""

from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.http import Http404, HttpResponseRedirect
from django.db import transaction
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from os.path import exists
from os import makedirs
from datetime import datetime
from random import choice
import string

from upload.forms import DataInputForm
from excel.headers import *
from excel.handlers import BSExcelFileData
from BS.settings import MEDIA_ROOT

from etat_civil.models import EtatCivil
from international.models import Pays
from admission.models import Admission, FiliereAdmission, DomaineAdmission

@transaction.commit_on_success
def upload(request):
    """Manage the uploading of new data and storing in the Database"""
    
    if request.method == 'POST':
        form = DataInputForm(request.POST, request.FILES)
        if form.is_valid():
            # ALL THE  MAGIC HAPPENS HERE
            upload, errors = populate_database(request.FILES['file'])
            if len(errors)==0:
                return HttpResponseRedirect('success/')
            else:
                return render_to_response('upload/upload.html', RequestContext(request,{'form': form, 'errors': errors}))
    else:
        form = DataInputForm()
    return render_to_response('upload/upload.html', RequestContext(request,{'form': form}))

def save_excel(file):
    """Save the input excel file in the /static/upload/ directory"""
    # EXCEL SAVE PATH
    filepath = MEDIA_ROOT+'/upload/'
    filename = 'tmp_xl_data.xls'
    if not exists(filepath):
        makedirs(filepath)   
        
    # SAVE EXCEL FILE
    with open(filepath+filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return destination

def create_etat_civil(row):
    """Read an excel row and save the corresponding EtatCivil object in database"""
    errors = []
    nationalite, created = Pays.objects.get_or_create(nom=unicode(row['nationalite']))            
    ec = EtatCivil()
    ec.nom_insa = row['nom_insa']
    ec.nom_actuel = row['nom_actuel']
    ec.prenom =row['prenom']
    ec.num_etudiant = row['num_etudiant']
    ec.sexe = row['sexe']
    ec.date_naissance = datetime(*[int(i) for i in row['date_de_naissance'].split("/")][::-1])
    ec.nationalite = nationalite # MUST BE A "PAYS" INSTANCE
    ec.adresse_1 = row['adresse_1_(personnelle)']
    ec.zip_adresse_1 = row['code_postal_1']
    ec.adresse_2 = row['adresse_2_(parentale)']
    ec.zip_adresse_2 = row['code_postal_2']
    ec.email_1 = row['email_1']
    ec.email_2 = row['email_2']
    try:
        ec.full_clean()
    except ValidationError, e:
        m = dict(e.message_dict)
        errors.append([str("%s %s"%(ec.prenom, ec.nom_insa)), [list(k) for k in zip(m.keys(),m.values())]])

    return ec, errors 
            
def create_user(etat_civil):
    """Create user associated with an etat civil"""
    errors = []
    us = User()
    us.username = etat_civil.prenom[0].lower() + etat_civil.nom_insa.lower()
    chars = string.ascii_letters + string.digits
    us.password = "".join(choice(chars) for x in range(8))
    try:
        us.full_clean()
    except ValidationError, e:
        m = dict(e.message_dict)
        errors.append([str("%s %s"%(etat_civil.prenom, etat_civil.nom_insa)), [list(k) for k in zip(m.keys(),m.values())]])  
    return us, errors                      
    
def create_admission(row, etat_civil):
    """Read an excel row and save the corresponding Admission object in database"""
    errors = []
    ad = Admission()
    ad.filiere_org = FiliereAdmission.objects.get_or_create(nom=row['origine_avant_BIM'])[0]
    ad.domaine_org = DomaineAdmission.objects.get_or_create(nom=row['filiere_avant_BIM'])[0]
    ad.annee_admission = row['annee_admission']
    ad.rang_pre_BS = row['classement_avant_BIM']
    ad.taille_promo_pre_BS = row['taille_de_promo_avant_BIM']
    try:
        ad.full_clean()
    except ValidationError, e:
        m = dict(e.message_dict)
        errors.append([str("%s %s"%(etat_civil.prenom, etat_civil.nom_insa)), [list(k) for k in zip(m.keys(),m.values())]])  
    return ad, errors                      
    
 
def populate_database(file):
    """
    Save the input excel file in the /MEDIA_ROOT/upload/ directory,
    instanciate database-compliant objects and populate database
    """
    xl = BSExcelFileData(save_excel(file).name)
    sheet = 0
    rowmax = xl.get_corners(sheet)[-1]
 
    errors = []
    upload = True # If upload still True at the end, --> save

    for nrow in range (1, rowmax+1): 
        row = xl.get_row(sheet, nrow)
        
        # ETAT CIVIL
        ec, e = create_etat_civil(row)
        if len(e) > 0:errors.append(e)
            
        # USER
        us, e = create_user(ec)    
        if len(e) > 0:errors.append(e)
        
        # ADMISSION
        ad, e = create_admission(row, ec)
        if len(e) > 0:errors.append(e)
        
    if len(errors)==0:
        upload = False
    else:
        upload = True
    return (upload, errors)


    
    
    

