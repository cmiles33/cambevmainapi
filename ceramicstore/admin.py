from django.contrib import admin
from .models import Collection, Product, CollectionBlogPost, ProductPictures

# Register your models here.


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(CollectionBlogPost)
class CollectionBlogPost(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'status')
    list_filter = ('status', 'created', 'publish')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(ProductPictures)
class ProductPictures(admin.ModelAdmin):
    list_display = ['name', 'slug',
                    'created',]
    list_filter = ['created', ]
    prepopulated_fields = {'slug': ('name',)}
