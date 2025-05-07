from django import forms
from .models import Contact

class ContactCreationForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'full_name','email','phone_number','subject','message'
        )
        widgets = {
            'full_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Full Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Phone Number'}),
            'subject':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Subject'}),
            'message':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Message'}),
        }