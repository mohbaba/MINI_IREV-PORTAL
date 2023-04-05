from django.shortcuts import render , redirect
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'poll_unit_result.html')