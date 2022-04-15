from django.db import models
# Create your models here.


##Class for product manage images
class Image(models.Model):
    url = models.CharField(max_length=170)
    slug = models.SlugField(max_length=200)
 

##This class is for insert product attributes
class Attribute(models.Model):
    title = models.CharField(max_length=55)
    value = models.CharField(max_length=55)


##This class is for insert witch product attribut that can change product price 
class MainAttribute(models.Model):
    title = models.CharField(max_length=55)
    value = models.CharField(max_length=55)
    other_attributs= models.ManyToManyField(Attribute)


##This class is for products category
class Category(models.Model):
    title = models.CharField(max_length=55)
    slug = models.SlugField(max_length=75)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)


##This class is for products
class Product(models.Model):
    title = models.CharField(max_length=150)
    brand = models.CharField(max_length=50)
    slug = models.SlugField(max_length=285)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    main_img = models.CharField(max_length=700)
    images= models.ManyToManyField(Image, blank=True, null=True)
    main_attribute = models.ManyToManyField(MainAttribute, blank=True, null=True)
    attributes = models.ManyToManyField(Attribute, blank=True, null=True)
    description = models.TextField()
    status = models.BooleanField(default=True)

##Eache category filter value for title
class FilterValue(models.Model):
    title = models.CharField(max_length=85)
    slug = models.CharField(max_length=100)

##Eache category filters title
class FilterItem(models.Model):
    title = models.CharField(max_length=85)
    value = models.ManyToManyField(FilterValue)
    slug = models.SlugField(max_length=100)


##This class will use for handel products search filter base on thier category
class Filter(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    filters = models.ManyToManyField(FilterItem)