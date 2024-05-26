from django.shortcuts import render
from django.http import HttpResponse
from .models import Shargalka  # Modul nomini to'g'ri yozing

def index(request):
    soz = request.GET.get('q', '')
    if soz != '':
        natija = Shargalka.objects.filter(savol__contains=soz).all()[:3]
    else:
        natija =None

    return render(request, 'index.html', {'q': soz, 'natija':natija})

def salom2(request):
    return HttpResponse('<h1>salom<h1>')  # HttpResponse ni return qilish kerak
