from django.shortcuts import render
from .models import product

# Create your views here.
def product_list(request):
    products = product.objects.all()
    # return render(request, 'product_list.html', {'products': products})
    context = {
       'products':products,
    }
    return render(request, 'firstapp/product_list.html', context)