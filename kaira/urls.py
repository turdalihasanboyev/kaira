from django.urls import path

from .api.SubEmail.SubEmailLC.views import SubEmailLCAPIView
from .api.SubEmail.SubEmailRUD.views import SubEmailRUDAPIView

from .api.Testimonial.TestimonialLC.views import TestimonialLCAPIView
from .api.Testimonial.TestimonialRUD.views import TestimonialRUDAPIView

from .api.Category.CategoryLC.views import CategoryLCAPIView
from .api.Category.CategoryRUD.views import CategoryRUDAPIView


urlpatterns = [
    path('sub-email-lc/', SubEmailLCAPIView.as_view(), name='sub-email-lc'),
    path('sub-email-rud/<int:pk>/', SubEmailRUDAPIView.as_view(), name='sub-email-rud'),

    path('testimonial-lc/', TestimonialLCAPIView.as_view(), name='testimonial-lc'),
    path('testimonial-rud/<int:pk>/', TestimonialRUDAPIView.as_view(), name='testimonial-rud'),

    path('category-lc/', CategoryLCAPIView.as_view(), name='category-lc'),
    path('category-rud/<int:pk>/', CategoryRUDAPIView.as_view(), name='category-rud'),
]
