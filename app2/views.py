from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vista1_app2(request):
    return HttpResponse("<h1>Hola desde vista 1 app2</h1>")
