from django.contrib import admin
from . import models
# Register your models here.


##Register Image model to admin panel
@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image',)


##Register Attribute model to admin panel
@admin.register(models.Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('title','value')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('title',)


##Register MainAttribute model to admin panel
@admin.register(models.MainAttribute)
class MainAttributeAdmin(admin.ModelAdmin):
    list_display = ('title','value')
    search_fields = ('title',)


##Register Category model to admin panel
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    # parent
    list_display = ('title',)
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('title',)


##Register Product model to admin panel
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    # parent
    list_display = ('title','status')
    prepopulated_fields = {'slug':('title','brand')}
    search_fields = ('title',)


##Register FilterValue model to admin panel
@admin.register(models.FilterValue)
class FilterValueAdmin(admin.ModelAdmin):
    # parent
    list_display = ('title',)
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('title',)


##Register FilterItem model to admin panel
@admin.register(models.FilterItem)
class FilterItemAdmin(admin.ModelAdmin):
    # parent
    list_display = ('title',)
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('title',)


##Register Filter model to admin panel
@admin.register(models.Filter)
class FilterAdmin(admin.ModelAdmin):
    # parent
    list_display = ('category',)
    # prepopulated_fields = {'slug':('title',)}
    # search_fields=('category[title]',)

