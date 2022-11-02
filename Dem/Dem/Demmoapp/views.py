from django.http import HttpResponse
from django.shortcuts import render
from .models import Places

# Create your views here.
def rag(request):
    obj=Places.objects.all()
    return render(request,'index.html',{'result':obj})





