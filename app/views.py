from django.shortcuts import render
from app.models import Document

# Create your views here.

def home(request):
    d = Document.objects.all()
    return render(request, 'home.html', {"documents": d})