from django.shortcuts import render
from django.views import View
from django.conf import settings
from . import models
# Create your views here.


###This function will add media to context as default
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


##This class will show each product page
class Product(View):
    def get(self, request,product_id,product_slug):
        #Find wich product that id is same as the id entered in url bar
        product=models.Product.objects.filter(id=product_id)
        #With this function we gonna have categories in a list from parent to child
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

##With this class u could search products by category in url
class Category(View):
    def get(self, request,category_slug):
        #Get all products
        products=models.Product.objects.all()
        #Wich products those have same category as searches category will add to this list
        search=[]
        #With this function we could find products thier have wich category we search
        def Category(category):
            #If lastest category was what we want add it , else check parent category
            if category.slug == category_slug:
                search.append(product)
            else:
                if category.parent != None:
                    Category(category.parent)  
        for product in products:
            Category(product.category)

        context={'products':search}
        return render(request, 'shop/search.html',context)