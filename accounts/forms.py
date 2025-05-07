from django import forms
from .models import (
    CustomUser
)

class UsercreationForm(forms.ModelForm):
    password2 = forms.CharField(
        max_length=128,required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirmation Password'})
    )
    class Meta:
        model = CustomUser
        fields = (
            'username','email','first_name','last_name','avatar','phone_number','birth_date',
            'password','password2'
        )
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),
            'avatar': forms.FileInput(attrs={'class':'form-control'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Phone Number'}),
            'birth_date': forms.DateInput(attrs={'class':'form-control','placeholder':'Enter Phone Birth Date'}),
            'password': forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}),
        }
    def clean_username(self):
        username = self.cleaned_data['username']

        if CustomUser.objects.filter(username = username).exists():
            raise forms.ValidationError("This username already taken.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']

        if CustomUser.objects.filter(email = email).exists():
            raise forms.ValidationError("This email already taken.")
        return email
    
    def clean(self):
        cleaned_data =  super().clean()
        password1 = cleaned_data.get('password',"")
        password2 = cleaned_data.get('password2',"")

        if not password1 or not password2:
            raise forms.ValidationError("your must set your password.")
        
        if len(password1)<8:
            raise forms.ValidationError("your password must be at least char.")
        
        if password1 != password2:
            raise forms.ValidationError("your password must be same with confirmation password.")
        
        return cleaned_data
    
    def save(self, commit = ...):
        user =  super().save(commit)
        if commit:
            user.set_password(self.cleaned_data['password'])
            user.save()
        return user