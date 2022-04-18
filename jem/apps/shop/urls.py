from django.urls import path
from . import views

urlpatterns =[
    path('',views.Index.as_view(),name='home'),
    path('search/',views.Shop.as_view(),name='shop'),
    path('search/p<int:product_id>-<slug:product_slug>',views.Product.as_view(),name='product'),
]
