from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

from .models import Publication, Editorial, Home, Contact, Prose, Interview, About, AboutPDF


# Create your views here.

def home(request):
    home = Home.objects.all()
    return render(request, 'home.html', {'home': home})

def contact(request):
    contact_content = Contact.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send the email
            subject = f"{subject }"
            body = f"Subject: {subject}\nEmail: {email}\nMessage: {message}"
            send_mail(subject, body, email, ['kenjitsuchiya1@gmail.com'])

            # Optionally, redirect to a success page after sending the email
            # return redirect('success_page')  # Don't forget to define the URL for the success page
    else:
        form = ContactForm()


    return render(request, 'contact.html', {'contact': contact_content, 'form': form})

def publication(request):
    publication = Publication.objects.all()
    return render(request, 'publication.html', {'publication': publication})

def editorial(request):
    editorials = Editorial.objects.all()
    return render(request, 'editorial.html', {'editorials': editorials})

def prose(request):
    prose = Prose.objects.all()
    return render(request, 'prose.html', {'prose': prose})

def interview(request):
    interviews = Interview.objects.all()
    return render(request, 'interview.html', {'interview': interviews})

def about(request):
    about = About.objects.all()
    about_pdfs = AboutPDF.objects.all()
    context = {
        'about': about,
        'about_pdfs': about_pdfs,
    }

    return render(request, 'about.html', context)

