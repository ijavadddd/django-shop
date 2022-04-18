from django.db import models
# Create your models here.


##Class for product manage images
class Image(models.Model):
    url = models.CharField(max_length=170)
    slug = models.SlugField(max_length=200)
    
    def __str__(self):
        info = f'{self.slug}'
        return info


##This class is for insert product attributes
class Attribute(models.Model):
    title = models.CharField(max_length=55)
    slug = models.SlugField(max_length=70)
    value = models.CharField(max_length=55)
    
    def __str__(self):
        info = f'{self.title} : {self.value}'
        return info


##This class is for insert witch product attribut that can change product price 
class MainAttribute(models.Model):
    title = models.CharField(max_length=55)
    value = models.CharField(max_length=55)
    other_attributs= models.ManyToManyField(Attribute)

    def __str__(self):
        info = f'{self.title} : {self.value}'
        return info


##This class is for products category
class Category(models.Model):
    title = models.CharField(max_length=55)
    slug = models.SlugField(max_length=75)
    parent = models.ForeignKey('self', on_delete=models.CASCADE ,null=True ,blank=True, default=None)
    
    def __str__(self):
        info = f'{self.title}'
        return info


##This class is for products
class Product(models.Model):
    title = models.CharField(max_length=150)
    brand = models.CharField(max_length=50, null=True, blank=True, default=None)
    slug = models.SlugField(max_length=285)
    price = models.IntegerField()
    discount = models.IntegerField(blank=True ,null=None , default=0)
    
    def New_Price(self):
        new_price = (self.price * self.discount)/100
        new_price = self.price - new_price
        return new_price

    new_price = New_Price
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    main_img = models.CharField(max_length=700)
    images= models.ManyToManyField(Image, blank=True, null=True)
    main_attribute = models.ManyToManyField(MainAttribute, blank=True, null=True)
    attributes = models.ManyToManyField(Attribute, blank=True, null=True)
    description = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        info = f'{self.title} {self.brand} - {self.status}'
        return info


##Eache category filter value for title
class FilterValue(models.Model):
    title = models.CharField(max_length=85)
    slug = models.CharField(max_length=100)

    def __str__(self):
        info = f'{self.title}'
        return info

##Eache category filters title
class FilterItem(models.Model):
    title = models.CharField(max_length=85)
    value = models.ManyToManyField(FilterValue)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        info = f'{self.title}'
        return info

##This class will use for handel products search filter base on thier category
class Filter(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    filters = models.ManyToManyField(FilterItem)

    def __str__(self):
        info = f'{self.title}'
        return info