from django.shortcuts import render,redirect
from .forms import (
    ContactCreationForm
)
# Create your views here.

def home_view(request):
    return render(request,'home.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactCreationForm(request.POST)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user if request.user.is_authenticated else None
            contact.save()
            return redirect('home')
        return render(request,'contact.html',{'form':form})
    form = ContactCreationForm()
    return render(request,'contact.html',{'form':form})