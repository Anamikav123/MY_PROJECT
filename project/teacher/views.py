from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import AddMarkForm,AddStudentForm
from django.http import HttpResponse
from django.contrib import messages
from.models import StudentModel


# Create your views here.

class AddMark(View):
    def get(self,request,*args,**kwargs):
        f=AddMarkForm()
        return render(request,"addmark.html",{"form":f})
    def post(self,request,*args,**kwargs):
        form_data=AddMarkForm(data=request.POST)
        if form_data.is_valid():
                 m1=form_data.cleaned_data.get("mark1")
                 m2=form_data.cleaned_data.get("mark2")
                 m3=form_data.cleaned_data.get("mark3")
                 m4=form_data.cleaned_data.get("mark4")
                 m5=form_data.cleaned_data.get("mark5")
                 mark=int(m1)+int(m2)+int(m3)+int(m4)+int(m5)
                 return render (request,"addmark.html",{"res":mark})
        else:
                 return render(request,"addmark.html",{"form":form_data})
            
  
class AddStudent(View):
    def get(self,request,*args,**kwargs):  
      f1=AddStudentForm() 
      return render(request,"addstu.html",{"form":f1})
    def post(self,request,*args,**kwargs):
        form_data=AddStudentForm(data=request.POST)
        if form_data.is_valid():
            fn=form_data.cleaned_data.get("first_name")
            ln=form_data.cleaned_data.get("last_name")
            ph=form_data.cleaned_data.get("phone")
            age=form_data.cleaned_data.get("age")
            email=form_data.cleaned_data.get("email")
            address=form_data.cleaned_data.get("Address")
            StudentModel.objects.create(first=fn,last=ln,age=age,phone=ph,email=email,Address=address)

            messages.success(request,"Student added successfully!!!")
            return redirect("h")
            
        else:
             messages.success(request,"failed to  add Student!!!")
             return render(request,"addstu.html",{"form":form_data})
class StudentListView(View):
    def get(self,request,*args,**kwargs):
        #res="Anamika"
        res=StudentModel.objects.all()
        return render(request,"ViewStud.html",{"data":res})
class StudentDeleteView(View):
    def get(self,request,*args,**kwargs):
        sid=kwargs.get("ssid")
        stu=StudentModel.objects.get(id=sid)
        stu.delete()
        return redirect("viewstu")
class StudentEditView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("sid")
        stu=StudentModel.objects.get(id=id)
        f=AddStudentForm(initial={"first_name":stu.first,"last_name":stu.last,"age":stu.age,"email":stu.email,"Address":stu.Address,"phone":stu.phone})
        return render(request,"editstu.html",{"form":f})
    def post(self,request,*args,**kwargs):
        form_data=AddStudentForm(data=request.POST)
        if form_data.is_valid():
            fn=form_data.cleaned_data.get("first_name")
            ln=form_data.cleaned_data.get("last_name")
            ph=form_data.cleaned_data.get("phone")
            age=form_data.cleaned_data.get("age")
            email=form_data.cleaned_data.get("email")
            address=form_data.cleaned_data.get("Address")
            id=kwargs.get("sid")
            stu=StudentModel.objects.get(id=id)
            stu.first=fn
            stu.last=ln
            stu.phone=ph
            stu.age=age
            stu.Address=address
            stu.email=email
            stu.save()
            messages.success(request,"Student details updated successfully!!")
            return redirect("viewstu")
        else:
            messages.error(request,"updation failed")
            return render(request,"editstu.html",{"form":form_data})







