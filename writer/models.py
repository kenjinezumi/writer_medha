from django.db import models

class Home(models.Model):
    title = models.TextField(null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Home - {}".format(self.title)

class Contact(models.Model):
    title = models.TextField(null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Contact - {}".format(self.title)

class Publication(models.Model):
    title = models.TextField(null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Publication - {}".format(self.title)

class Editorial(models.Model):
    title = models.TextField(null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Editorial - {}".format(self.title)

class Prose(models.Model):
    title = models.TextField(null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Prose - {}".format(self.title)

class Interview(models.Model):
    title = models.TextField(null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Interview - {}".format(self.title)

class About(models.Model):
    title = models.TextField(null=True)
    content = models.TextField()

    def __str__(self):
        return "About - {}".format(self.title)


class AboutPDF(models.Model):
    title = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='about_pdfs/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title