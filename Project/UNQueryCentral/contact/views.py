# contact/views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            full_message = f"Message from {name} ({email}):\n\n{message}"
            email_subject = f"Nouveau Mail de la part de {email} depuis UNQueryCentral"
            
            send_mail(
                email_subject,
                full_message,
                email,  # From email
                [settings.DEFAULT_FROM_EMAIL],  # To email
            )
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('/contact/?success=true')  # Rediriger avec le paramètre 'success'
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})
