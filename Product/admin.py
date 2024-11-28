from django.contrib import admin
from Product.models import Category,Product,Images


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','title','image_tag','created_at','updated_at']
admin.site.register(Category, CategoryAdmin)



class ImagesAdmin(admin.ModelAdmin):
    list_display = ['id','title']
admin.site.register(Images, ImagesAdmin)

class productImageInline(admin.TabularInline):
    model = Images
    extra = 5


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','image_tag', 'status', 'created_at', 'updated_at']
    list_filter = ['title', 'created_at']
    list_per_page = 10
    search_fields = ['title', 'new_price', 'detail']
    inlines = [productImageInline]
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Product, ProductAdmin)