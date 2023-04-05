from django.urls import path , include
from poll_unit_result.views import *


urlpatterns = [
    path('', index,name = 'result')
]