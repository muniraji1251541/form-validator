from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def form_valid(request):
    fo=Form_validator()
    d={'form':fo}
    if request.method=='POST':
        fd=Form_validator(request.POST)
        if fd.is_valid():
            return HttpResponse(str(fd.cleaned_data))
    return render(request,'form_valid.html',d)