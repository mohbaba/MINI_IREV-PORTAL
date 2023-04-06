from django.shortcuts import render , redirect
from poll_unit_result.models import *
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method == 'GET':
        results = request['q']
        
        if results:
            final_results = AnnouncedPuResults.objects.filter(name__icontains = results)
        
        else:
            final_results = AnnouncedPuResults.objects.all()
    pu_results = AnnouncedPuResults.objects.all()
    return render(request, 'poll_unit_result.html')