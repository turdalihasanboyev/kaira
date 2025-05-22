from django.urls import path

from .api.SubEmail.SubEmailLC.views import SubEmailLCAPIView
from .api.SubEmail.SubEmailRUD.views import SubEmailRUDAPIView

from .api.Testimonial.TestimonialLC.views import TestimonialLCAPIView
from .api.Testimonial.TestimonialRUD.views import TestimonialRUDAPIView

from .api.Category.CategoryLC.views import CategoryLCAPIView
from .api.Category.CategoryRUD.views import CategoryRUDAPIView

from .api.Blog.BlogLC.views import BlogLCAPIView
from .api.Blog.BlogRUD.views import BlogRUDAPIView

from .api.Product.ProductLC.views import ProductLCAPIView
from .api.Product.ProductRUD.views import ProductRUDAPIView


urlpatterns = [
    path('sub-email-lc/', SubEmailLCAPIView.as_view(), name='sub-email-lc'),
    path('sub-email-rud/<int:pk>/', SubEmailRUDAPIView.as_view(), name='sub-email-rud'),

    path('testimonial-lc/', TestimonialLCAPIView.as_view(), name='testimonial-lc'),
    path('testimonial-rud/<int:pk>/', TestimonialRUDAPIView.as_view(), name='testimonial-rud'),

    path('category-lc/', CategoryLCAPIView.as_view(), name='category-lc'),
    path('category-rud/<int:pk>/', CategoryRUDAPIView.as_view(), name='category-rud'),

    path('blog-lc/', BlogLCAPIView.as_view(), name='blog-lc'),
    path('blog-rud/<int:pk>/', BlogRUDAPIView.as_view(), name='blog-rud'),

    path('product-lc/', ProductLCAPIView.as_view(), name='product-lc'),
    path('product-rud/<int:pk>/', ProductRUDAPIView.as_view(), name='product-rud'),
]
