from django.http import HttpResponse
from django.shortcuts import render
from .models import  Author, Entry
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
       # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={},
    )