from django import forms

class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=80)
    middle_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    address = forms.CharField(max_length=255)
    date_of_birth = forms.DateField()
    phone_number = forms.CharField(max_length=13)
    date = forms.DateField()
    occupation = forms.CharField(max_length=80)
