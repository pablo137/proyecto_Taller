from django.shortcuts import render
from .models import Emprendedor


def index(request):
    emprendedores = Emprendedor.objects.all()
    context = { 'emprendedores' : emprendedores }
    return render(request, "index.html", context)
