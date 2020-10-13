from django.shortcuts import render

def index(request):

    # articles = ["1", "2","3"]
    # context = {
    #     'articles': articles
    # }
    return render(request,"club/index.html")