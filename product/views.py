from django.shortcuts import render
from .forms import *
# Create your views here.
def IndexView(request):
    return render(request, 'product/index.html', )


def AddProductView(request):
    forms = AddProductForm()
    return render(request,  'product/add_product.html', {'form': forms})
