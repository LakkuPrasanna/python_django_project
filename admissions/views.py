from django.shortcuts import render
from admissions.models import Admission
# Create your views here.
def home(request):
    # return render(request,'home.html',{})
    data=Admission.objects.all()
    res=render(request,'home.html',{'data':data})
    return res
def index(request):
    return render(request,'index.html',{})
def products(request):
    return render(request,'Products.html',{})
def login(request):
    return render(request,'Login.html',{})
def profiles(request):
    return render(request,'Profiles.html',{})
def services(request):
    return render(request,'Services.html',{})
def transport(request):
    return render(request,'Transport.html',{})