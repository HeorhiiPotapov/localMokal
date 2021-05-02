from django.contrib import admin
from .models import Category, Product, Image
from mptt.admin import DraggableMPTTAdmin


admin.site.register(Category,
                    DraggableMPTTAdmin,

                    list_display=(
                        'tree_actions',
                        'indented_title',
                    ),
                    list_display_links=(
                        'indented_title',
                    ),
                    model=Category,
                    fields=('name', 'slug', 'image', 'parent', 'is_active'),
                    prepopulated_fields={'slug': ('name', )},
                    mptt_level_indent=30)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_filter = ('category', 'city', 'is_active', 'timestamp')

    fields = ['main_image',
              'video',
              'owner',
              'name',
              'city',
              'category',
              'price',
              'overview',
              'discount',
              'is_active',
              'timestamp',
              'discount_expiry']
    list_display = ('name',
                    'category',
                    'price',
                    'is_active')
    inlines = [ImageInline, ]
