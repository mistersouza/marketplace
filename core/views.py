from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def item(request):
    return render(request, 'item.html')

def contact(request):
    return render(request, 'contact.html')