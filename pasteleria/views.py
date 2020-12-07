from django.shortcuts import render
from .models import Cake
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def tortas(request):
    cakes = Cake.objects.all()

    page = request.GET.get('page',1)
    paginator = Paginator(cakes,3)

    try:
        cakes = paginator.page(page)
    except PageNotAnInteger:
        cakes = paginator.page(1)
    except EmptyPage:
        cakes = paginator.page(paginator.num_pages)

    return render(request, "pasteleria/tortas.html",{'cakes':cakes})
