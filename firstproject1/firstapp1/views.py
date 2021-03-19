from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show(request):
    return HttpResponse("<h1>Hello Hai!!!</h1>")



def teju(x):
    return HttpResponse('<h2 style="color: red">Myself is Tejaswini</h2>\n<h3>myself is teju</h3>\n<h4>myself is tej</h4>')