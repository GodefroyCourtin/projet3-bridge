from django.shortcuts import render

def index(request):
    return render(request,"club/index.html")

def article(request):
    return render(request,"club/article.html")

def contact(request):
    return render(request,"club/contact.html")

def agenda(request):
    return render(request,"club/agenda.html")
