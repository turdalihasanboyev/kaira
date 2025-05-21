from django.db import models
from django.core.validators import MinValueValidator


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


class Product(BaseModel):
    CURRENCY_SYMBOLS = {
    'USD': '$',
    'EUR': '€',
    'UZS': "so'm",
    'RUB': '₽',
    }
    name = models.CharField(max_length=250, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category', limit_choices_to={'role': CategoryRole.PRODUCT})
    image = models.ImageField(upload_to='product_images', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    currency = models.CharField(max_length=3, choices=CURRENCY_SYMBOLS.items())

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    @property
    def display_price(self):
        symbol = self.CURRENCY_SYMBOLS.get(self.currency)
        return f'{self.price} {symbol}'
    
    def __str__(self):
        return f'{self.name} {self.display_price}'


class Blog(BaseModel):
    name = models.CharField(max_length=250, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blog_category', limit_choices_to={'role': CategoryRole.BLOG})
    image = models.ImageField(upload_to='blog_images', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return f'{self.name}'
