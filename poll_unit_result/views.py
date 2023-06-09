from django.shortcuts import render , redirect
from poll_unit_result.models import *
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method == 'GET':
        final_results = None
        results = request.GET.get('q','')
        
        if results:
            final_results = PollingUnit.objects.filter(polling_unit_number__icontains = results)
            poll_objects = final_results.values('polling_unit_id','polling_unit_name')
            
        
        else:
            finally_results = AnnouncedPuResults.objects.all()

    context = {'results':results, 'final_results': final_results, 'poll_objects': poll_objects}

    return render(request, 'poll_unit_result.html',context)