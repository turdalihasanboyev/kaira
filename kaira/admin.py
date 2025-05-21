from django.contrib import admin


admin.site.site_header = 'kaira Admin Panel'
admin.site.site_title = 'kaira Admin Panel'
admin.site.index_title = 'Welcome to kaira Admin Panel'


from .models import (
    SubEmail,
    Testimonial,
    Category,
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
        'testimonial',
        'created_at',
        'updated_at',
    )
    search_fields = ('author', 'testimonial',)


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
    search_fields = ('name', 'role',)
    list_filter = ('role',)
