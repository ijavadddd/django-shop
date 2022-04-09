from django.shortcuts import render
from django.views import View
# Create your views here.


###This class will render home page
class Index(View):
    def get(self,request):
        return render(request, 'shop/index.html')

###This class will show products and search results
class Search(View):
    def get(self,request):
        return render(request, 'shop/search.html')