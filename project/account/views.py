from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from .forms import LoginForm,RegisterForm
from django.http import HttpResponse


class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"main.html")
class RegView(View):
    def get(self,request,*args,**kwargs):
        f=RegisterForm()
        form_data=RegisterForm(data=request.POST)
        if form_data.is_valid():
          return render(request,"reg.html",{"form":f})
        else:
            return HttpResponse("invalid")
class LogView(View):
    def get(self,request,*args,**kwargs):
        f=LoginForm()
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid:
         return render(request,"login.html",{"form":f})
        else:
            return  HttpResponse("invalid")

