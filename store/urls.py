from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products_list),
    path('products/<int:pk>/', views.product_detail),
    path('category/<int:pk>/', views.category_detail, name='category-detail')
]
