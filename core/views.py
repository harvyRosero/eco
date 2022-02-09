from django.conf import settings
from django.shortcuts import render
from django.views import generic
from .forms import ContactForm
from django.urls import reverse 
from django.core.mail import send_mail
from django.contrib import messages

class HomeView(generic.TemplateView):
    template_name = 'index.html'
    
class ContantView(generic.FormView):
    
    form_class = ContactForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse('contact')
    
    def form_valid(self, form):
        messages.info(
            self.request, 'Thank you for your message. We will contact you soon!')
        
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        
        full_message = f"""
            message from {name} {email}:
            ____________________________
            
            
            {message}
            
            """
            
        send_mail(
            subject= "Message from Contact Form",
            message = full_message,
            from_email= settings.DEFAULT_FROM_EMAIL,
            recipient_list= [settings.NOTIFY_EMAIL],
            )
        
        return super(ContantView, self).form_valid(form)