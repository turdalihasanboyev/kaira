from django.contrib import admin


admin.site.site_header = 'kaira Admin Panel'
admin.site.site_title = 'kaira Admin Panel'
admin.site.index_title = 'Welcome to kaira Admin Panel'


from .models import (
    SubEmail,
    Testimonial,
    Category,
    Blog,
    Product,
)


@admin.register(SubEmail)
class SubEmailAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'created_at',
        'updated_at',
    )
    search_fields = ('email',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'created_at',
        'updated_at',
    )
    search_fields = ('author',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'role',
        'image',
        'created_at',
        'updated_at',
    )
    search_fields = ('name',)
    list_filter = ('role',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'image',
        'created_at',
        'updated_at',
    )
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'image',
        'price',
        'currency',
        'display_price',
        'created_at',
        'updated_at',
    )
    search_fields = ('name',)
    list_filter = ('currency',)
