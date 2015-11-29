"""
Views for the cars app.
"""
from django.utils import simplejson as json
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import HttpResponseNotAllowed
from django.shortcuts import render_to_response
from cars.models import Car
from cars.forms import CarForm


def teststr(request):
     return render(request, 'dialogbox.html')
