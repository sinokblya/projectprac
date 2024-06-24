from django.contrib import admin
from .models import User
from django.contrib import admin
from .models import Product, Brand, Category, ProductMedia
from django.contrib import admin
from .models import CatalogSection, Category, Subcategory
from django.contrib import admin
from .models import News
from django.contrib import admin
from .models import Brand

admin.site.register(Brand)


admin.site.register(News)


admin.site.register(CatalogSection)
admin.site.register(Category)
admin.site.register(Subcategory)


admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ProductMedia)

admin.site.register(User)
