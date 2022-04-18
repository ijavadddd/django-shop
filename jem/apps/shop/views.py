from django.shortcuts import render
from django.views import View
from django.conf import settings
from . import models
# Create your views here.


###This class will render home page
def Media(request):
    context={
        'media':settings.MEDIA_URL,
    }
    return context


# This class will render home page
class Index(View):
    def get(self, request):
        return render(request, 'shop/index.html')


# This class will show products and search results
class Shop(View):
    def get(self, request):
        products=models.Product.objects.all()
        context={
            'products':products,
        }
        return render(request, 'shop/search.html',context)


# This class will show each product site
class Product(View):
    def get(self, request,product_id,product_slug):
        product=models.Product.objects.filter(id=product_id)
        Categories=[]
        def Category(category):
            if category.parent != None:
                Category(category.parent)
                Categories.append((category.slug,category.title))
            else:
                Categories.append((category.slug,category.title))

        Category(product[0].category)
        context={
            'product':product,
            'categories':Categories,
        }
        return render(request, 'shop/product.html',context)

class Category(View):
    def get(self, request,category_slug):
        products=models.Product.objects.all()
        search=[]
        def Category(category):
            if category.slug == category_slug:
                search.append(product)
            else:
                if category.parent != None:
                    Category(category.parent)  
        for product in products:
            Category(product.category)

        context={'products':search}
        return render(request, 'shop/search.html',context)