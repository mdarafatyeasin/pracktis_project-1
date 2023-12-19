from django.shortcuts import render

# Create your views here.
def appHome (request) :
    return render (request, 'appHome/appHome.html')

def home (request) :

    return render (request, 'home/home.html')

def about (request) :
    return render (request, 'about/about.html')

def contact (request) :
    return render (request, 'contact/contact.html')