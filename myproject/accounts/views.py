from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer, LoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import User
from .serializers import UserSerializer, UserDetailSerializer
from rest_framework import generics, permissions
from .models import Product, Brand, Category, ProductMedia
from .serializers import ProductSerializer, ProductCreateUpdateSerializer
from rest_framework import generics, permissions
from .models import CatalogSection, Category, Subcategory
from .serializers import CatalogSectionSerializer, CategorySerializer, SubcategorySerializer
import pandas as pd
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework import generics
from .models import News
from .serializers import NewsSerializer
from rest_framework import generics
from django.db.models import Q
from .models import Brand
from .serializers import BrandSerializer

class BrandListView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandSearchView(generics.ListAPIView):
    serializer_class = BrandSerializer

    def get_queryset(self):
        queryset = Brand.objects.all()
        name = self.request.query_params.get('name', None)
        country = self.request.query_params.get('country', None)
        category = self.request.query_params.get('category', None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        if country:
            queryset = queryset.filter(country__icontains=country)
        if category:
            queryset = queryset.filter(categories__icontains=category)
        return queryset


class NewsListView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class ImportCatalogDataView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        file = request.FILES['file']
        if not file.name.endswith('.xlsx'):
            return Response({"error": "File is not in Excel format"}, status=status.HTTP_400_BAD_REQUEST)
        
        df = pd.read_excel(file, engine='openpyxl')

        for _, row in df.iterrows():
            section_name = row['Раздел каталога']
            category_name = row['Название категории']
            subcategory_name = row['Название подкатегории']

            section, _ = CatalogSection.objects.get_or_create(name=section_name)
            category, _ = Category.objects.get_or_create(name=category_name, section=section)
            Subcategory.objects.get_or_create(name=subcategory_name, category=category)

        return Response({"success": "Data imported successfully"}, status=status.HTTP_201_CREATED)


class CatalogSectionListView(generics.ListCreateAPIView):
    queryset = CatalogSection.objects.all()
    serializer_class = CatalogSectionSerializer

class CatalogSectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CatalogSection.objects.all()
    serializer_class = CatalogSectionSerializer

class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubcategoryListView(generics.ListCreateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

class SubcategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateUpdateSerializer

class BrandListView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.ModelSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.ModelSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['username', 'email']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'middle_name']

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
