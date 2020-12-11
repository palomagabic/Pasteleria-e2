from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm

# Create your views here.
def contact(request):

    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')
            return redirect(reverse('contact') + "?OK")
        else:
            return redirect(reverse('contact') + "?FAIL")


    return render(request, "contact/contact.html",{'form':contact_form})
