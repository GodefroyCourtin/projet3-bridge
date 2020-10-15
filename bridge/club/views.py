from django.shortcuts import render

def index(request):
    return render(request,"club/index.html")

def article1(request):
    return render(request,"club/article1.html")

def article2(request):
    return render(request,"club/article2.html")

def article3(request):
    return render(request,"club/article3.html")

def contact(request):
    return render(request,"club/contact.html")

def agenda(request):
    return render(request,"club/agenda.html")

def galerie(request):
    return render(request,"club/galerie.html")

def evenement(request):
    return render(request,"club/evenement.html")