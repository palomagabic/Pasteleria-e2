from django.shortcuts import render

# Create your views here
def index(request):
    return render(request, "core/index.html")

def acerca_de(request):
    return render(request, "core/acerca_de.html")

def contacto(request):
    return render(request, "core/contacto.html")

def picoteo(request):
    return render(request, "core/picoteo.html")

def tortas(request):
    return render(request, "core/tortas.html")
