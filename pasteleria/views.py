from django.shortcuts import render

# Create your views here.
def tortas(request):
    return render(request, "pasteleria/tortas.html")
