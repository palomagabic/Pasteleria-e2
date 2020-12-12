from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.utils import timezone
from django.core.mail import EmailMessage
from .models import Form

# Create your views here.
def contact(request):
    contact_form = ContactForm(request.POST)

    if request.method == "POST":
        contact_form = ContactForm(data = request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')

            f =contact_form.save()

            email = EmailMessage(
            "Umami Pasteleria: Nuevo mensaje de contacto",
            "De {} <{}>\n\nEcribio:\n\n{}".format(name,email,message),
            "no-contestar@inbox.mailtrap.io",
            ["palo.cortes@alumnos.duoc.cl"],
            reply_to=[email]
            )

            try:
                email.send()
                return redirect(reverse('contact') + "?OK")
            except:
                return redirect(reverse('contact') + "?FAIL")


    return render(request, "contact/contact.html",{'form':contact_form})
