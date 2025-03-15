from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name="products"),
    path('create/', views.createProduct, name="create-product"),
    path('<str:pk>/', views.product, name="product"),
    path('edit/<str:pk>/', views.updateProduct, name="update-product"),
    path('delete/<str:pk>/', views.deleteProduct, name="delete-product"),


]
