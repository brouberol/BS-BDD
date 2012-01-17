# -*- coding: utf-8 -*-
"""
Forms related to data input
"""

from django import forms
from django.db.models import FileField
from django.core.exceptions import ValidationError

class DataInputForm(forms.Form):
    """Form allowing data input from an Excel file"""    
    file = forms.FileField()

    def clean_file(self):
        """ Check if the file exists and Excel formatted """
        
        file = self.cleaned_data['file']
        extension = str(file).split('.')[-1]
        if extension not in ['xls', 'xlsx']:
            raise ValidationError("Ce fichier doit être au format Excel (.xls, .xlsx)")
        else:
            return file
