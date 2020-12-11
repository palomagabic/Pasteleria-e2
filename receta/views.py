from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post, Category
from social.models import Link

# Create your views here.
def receta(request):
    posts = Post.objects.all()

    page = request.GET.get('page',1)
    paginator = Paginator(posts,1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "receta/receta.html",{'posts':posts})

def category(request, category_id):
    category = get_object_or_404(Category, id = category_id)
    return render(request, "receta/category.html", {'category':category})
