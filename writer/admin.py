from django.contrib import admin

from .forms import AboutPDFForm
from .models import Publication, Editorial, Prose, Interview, About, Contact, Home, AboutPDF
from django import forms




class AboutPDFAdmin(admin.ModelAdmin):
    form = AboutPDFForm
    list_display = ('title', 'created_at')

admin.site.register(Home)
admin.site.register(Publication)
admin.site.register(Editorial)
admin.site.register(Prose)
admin.site.register(Interview)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(AboutPDF)