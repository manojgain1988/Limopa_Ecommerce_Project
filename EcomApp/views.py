from django.shortcuts import render
from EcomApp .models import Setting
from Product .models import Product

# Create your views here.

def Home(request):
    setting = Setting.objects.get(id=1)
    sliding_images = Product.objects.all().order_by('id')[:3]
    latest_product = Product.objects.all().order_by('-id')
    products = Product.objects.all()
    
    context={
        'setting' : setting ,
        'sliding_images' : sliding_images ,
        'latest_product' : latest_product ,
        'products' : products ,
    }
    return render(request,'home.html',context)