from django.shortcuts import render
from .models import Distribution

def index(request):
    return render(request, 'index.html')

def distribution_list(request):
    distributions = Distribution.objects.all()
    return render(request, 'distribution_list.html', {'distributions': distributions})
