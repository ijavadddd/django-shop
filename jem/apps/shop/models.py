from django.db import models
# Create your models here.

class Image(models.Model):
    url = models.CharField(max_length=170)
    slug = models.SlugField(max_length=200)

class Attribute(models.Model):
    title = models.CharField(max_length=55)
    value = models.CharField(max_length=55)

class MainAttribute(models.Model):
    title = models.CharField(max_length=55)
    value = models.CharField(max_length=55)
    other_attributs= models.ManyToManyField(Attribute)

class Category(models.Model):
    title = models.CharField(max_length=55)
    slug = models.SlugField(max_length=75)
    parent = models.ForeignKey('self',on_delete=models.CASCADE)

class Product(models.Model):
    title = models.CharField(max_length=150)
    brand = models.CharField(max_length=50)
    slug = models.SlugField(max_length=285)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    main_img = models.CharField(max_length=700)
    images= models.ManyToManyField(Image, blank=True, null=True)
    main_attributes = models.ManyToManyField(MainAttribute,blank=True, null=True)
    attributes = models.ManyToManyField(Attribute, blank=True, null=True)
    description = models.TextField()
    status = models.BooleanField(default=True)