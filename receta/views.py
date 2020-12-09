from django.shortcuts import render
from .models import Post

# Create your views here.
def receta(request):
    posts = Post.objects.all()
    return render(request, "receta/receta.html",{'posts':posts})
