from django import forms
class AddMarkForm(forms.Form):
    mark1=forms.IntegerField(label="enter one mark")
    mark2=forms.IntegerField()
    mark3=forms.IntegerField()
    mark4=forms.IntegerField()
    mark5=forms.IntegerField()

    def clean(self):
        cleaned_data=super().clean()
        m1=cleaned_data.get("mark1")
        m2=cleaned_data.get("mark2")
        m3=cleaned_data.get("mark3")
        m4=cleaned_data.get("mark4")
        m5=cleaned_data.get("mark5")
        if m1<0:
            msg="mark canot be less than zero"
            self.add_error("mark1",msg)
        if m2<0:
            msg="mark canot be less than zero"
            self.add_error("mark2",msg)
        if m3<0:
            msg="mark canot be less than zero"
            self.add_error("mark3",msg)
        if m4<0:
            msg="mark canot be less than zero"
            self.add_error("mark4",msg)
        if m5<0:
            msg="mark canot be less than zero"
            self.add_error("mark5",msg)

class AddStudentForm(forms.Form):
    first_name=forms.CharField(max_length=25,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"enter your first name"}))
    last_name=forms.CharField(max_length=25,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"enter your last name"}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"enter your age"}))
    Address=forms.CharField(max_length=500,widget=forms.Textarea(attrs={"class":"form-control","placeholder":"enter your Address"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"enter your email"}))
    phone=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"enter your phone number"}))
    def clean(self):
        cleaned_data=super().clean()
        fn=cleaned_data.get("first_name")
        ln=cleaned_data.get("last_name")
        age=cleaned_data.get("age")
        ph=str(cleaned_data.get("phone"))
        email=cleaned_data.get("email")
        if fn==ln:
            self.add_error("last_name","first znd last name canot same")
        if age<1:
            self.add_error("age","age canot be zero")
        if len(ph)!=10:
            self.add_error("phone","phone number must be 10 digits")

    

