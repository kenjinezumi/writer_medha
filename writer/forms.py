# forms.py

from django import forms

from writer.models import AboutPDF


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=200, required=False, label="subject")
    email = forms.EmailField( required=False, label="email")
    message = forms.CharField(widget=forms.Textarea,  required=False, label="message")
    def clean(self):
        cleaned_data = super().clean()
        subject = cleaned_data.get('subject')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if self.is_bound:
            if not subject or not email or not message:
                raise forms.ValidationError("Please fill in all required fields.")

class AboutPDFForm(forms.ModelForm):
    class Meta:
        model = AboutPDF
        fields = ['title', 'pdf_file']