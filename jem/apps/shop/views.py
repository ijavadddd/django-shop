from django.shortcuts import render
from django.views import View
from django.conf import settings

# Create your views here.


###This class will render home page
def Media(request):
    context={
        'media':settings.MEDIA_URL,
    }
    return context


class Index(View):
    def get(self,request):
        return render(request, 'shop/index.html')

###This class will show products and search results
class Search(View):
    def get(self,request):
        return render(request, 'shop/search.html')