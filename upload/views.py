# -*- coding: utf-8 -*-
"""
Views related to data input
"""

from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.http import Http404, HttpResponseRedirect
from django.db import transaction

from upload.forms import DataInputForm

@transaction.commit_on_success
def upload(request):
    """Manage the uploading of new data and storing in the Database"""
    
    if request.method == 'POST':
        form = DataInputForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            print "File uploaded"
            return HttpResponseRedirect('/success/url/')
        else:
            print form.errors
    else:
        form = DataInputForm()
    return render_to_response('upload/upload.html', RequestContext(request,{'form': form}))
