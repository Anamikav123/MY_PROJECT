from django import forms

class LoginForm(forms.Form):
    Username=forms.CharField(max_length=50)
    Password=forms.CharField(max_length=25)
class RegisterForm(forms.Form):
    firstname=forms.CharField(max_length=50)
    lastname=forms.CharField(max_length=50)
    emailid=forms.EmailField()
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50)
    confirm_password=forms.CharField(max_length=50)