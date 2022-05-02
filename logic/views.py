from email import message
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Contact

# Create your views here.
class Homeviews(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-id']

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        contact = Contact()
        First_Name = request.POST.get('First_Name')
        Last_Name = request.POST.get('Last_Name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        message = request.POST.get('message')
        contact.first_name = First_Name
        contact.last_name = Last_Name
        contact.email = email
        contact.country = country
        contact.message = message
        contact.save()

        return render(request, "contact.html")

    return render(request, "contact.html")

class templates(ListView):
    model = Post
    template_name = 'templates.html'
    ordering = ['-id']
