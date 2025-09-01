from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("""
                        <h1>Hola mundo</h1>
                        <h2 style="color:blue">The best page!</h2>
                        """)

def saludo(request):
    return HttpResponse("<h1>Hellow</h1>")