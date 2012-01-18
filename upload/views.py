# -*- coding: utf-8 -*-
"""
Views related to data input
"""

from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.http import Http404, HttpResponseRedirect
from django.db import transaction

from os.path import exists
from os import makedirs
from datetime import datetime

from upload.forms import DataInputForm
from excel.headers import *
from excel.handlers import BSExcelFileData
from BS.settings import MEDIA_ROOT

from etat_civil.models import EtatCivil
from international.models import Pays

@transaction.commit_on_success
def upload(request):
    """Manage the uploading of new data and storing in the Database"""
    
    if request.method == 'POST':
        form = DataInputForm(request.POST, request.FILES)
        if form.is_valid():
            # ALL THE  MAGIC HAPPENS HERE
            populate_database(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = DataInputForm()
        return render_to_response('upload/upload.html', RequestContext(request,{'form': form}))

def save_excel(file):
    """Save the input excel file in the /static/upload/ directory"""
    filepath = MEDIA_ROOT+'/upload/'
    filename = 'tmp_xl_data.xls'
    if not exists(filepath):
        makedirs(filepath)           
    with open(filepath+filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return destination

def save_etat_civil(row):
    """Read an excel row and save the corresponding EtatCivil object in database"""

    nationalite, created = Pays.objects.get_or_create(nom=row['nationalite'])
    j,m,a = row['date_de_naissance'].split("/")
    j,m,a = int(j), int(m), int(a)    
    
    ec = EtatCivil()
    ec.nom_insa = row['nom_insa']
    ec.nom_actuel = row['nom_actuel']
    ec.prenom = row['prenom']
    ec.num_etudiant = row['num_etudiant']
    ec.sexe = row['sexe']
    ec.date_naissance = datetime(a,m,j) # LE PROBLEME VIENT DE LA, QUELQUE PART... BIUSOUS ET A DEMAIN
    # ec.date_naissance = row['date_de_naissance'] # LE BUG VIENT DE DATEFIELD QUI PART EN COUILLE. A DEMAIN =)
    # IDEA : change input format to string, or find a way to convert excel date --> datetime
    ec.nationalite = nationalite # MUST BE A "PAYS" INSTANCE
    ec.adresse_1 = row['adresse_1_(personnelle)']
    ec.zip_adresse_1 = row['code_postal_1']
    ec.adresse_2 = row['adresse_2_(parentale)']
    ec.zip_adresse_2 = row['code_postal_2']
    ec.email_1 = row['email_1']
    ec.email_2 = row['email_2']
    
    ec.save()
    
    
def populate_database(file):
    """
    Save the input excel file in the /MEDIA_ROOT/upload/ directory,
    instanciate database-compliant objects and populate database
    """
    xl = BSExcelFileData(save_excel(file).name)
    sheet = 0
    colmin, rowmin, colmax, rowmax = xl.get_corners(sheet)
    
    for nrow in range (1, rowmax+1):
        row = xl.select_row(sheet, nrow, colmax)
        print row
        save_etat_civil(row)
    
    
    
    

