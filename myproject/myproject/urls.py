"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (
    RegisterView, LoginView, UserListView, UserDetailView, UserUpdateView, UserDeleteView,
    ProductListView, ProductDetailView, BrandListView, CategoryListView,
    CatalogSectionListView, CatalogSectionDetailView, SubcategoryListView, SubcategoryDetailView,
    ImportCatalogDataView, NewsListView, NewsDetailView, BrandDetailView, BrandSearchView
)

urlpatterns = [
    # User URLs
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),

    # Product URLs
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    # Catalog URLs
    path('catalog/sections/', CatalogSectionListView.as_view(), name='catalog-section-list'),
    path('catalog/sections/<int:pk>/', CatalogSectionDetailView.as_view(), name='catalog-section-detail'),
    path('catalog/subcategories/', SubcategoryListView.as_view(), name='subcategory-list'),
    path('catalog/subcategories/<int:pk>/', SubcategoryDetailView.as_view(), name='subcategory-detail'),
    path('catalog/import/', ImportCatalogDataView.as_view(), name='import-catalog-data'),

    # News URLs
    path('news/', NewsListView.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),

    # Brand URLs
    path('brands/', BrandListView.as_view(), name='brand-list'),
    path('brands/<int:pk>/', BrandDetailView.as_view(), name='brand-detail'),
    path('brands/search/', BrandSearchView.as_view(), name='brand-search'),
]
