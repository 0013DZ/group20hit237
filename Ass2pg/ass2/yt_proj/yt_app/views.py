from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def list(request):
    return render (request, 'yt_app/list.html')

def homepage(request):
    return render (request, 'yt_app/homepage.html')