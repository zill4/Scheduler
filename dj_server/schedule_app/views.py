from django.http import HttpResponse
from django.shortcuts import render
from .models import  Person
# Create your views here.

def index(request):
    #return HttpResponse("<li><a href="{% url 'index' %}">Home</a></li>")
       # Render the HTML template index.html with the data in the context variable
    
    num_persons = Person.objects.count() 

    return render(
        request,
        'index.html',
        context={'num_persons':num_persons},
    )

