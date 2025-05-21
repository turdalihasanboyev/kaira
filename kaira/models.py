from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SubEmail(BaseModel):
    email = models.EmailField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Sub Email'
        verbose_name_plural = 'Sub Emails'

    def __str__(self):
        return f'{self.email}'


class Testimonial(BaseModel):
    author = models.CharField(max_length=150)
    testimonial = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return f'{self.author}'


class CategoryRole(models.TextChoices):
    BLOG = 'blog', 'Blog'
    PRODUCT = 'product', 'Product'


class Category(BaseModel):
    name = models.CharField(max_length=150, unique=True)
    role = models.CharField(max_length=10, choices=CategoryRole.choices)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'
