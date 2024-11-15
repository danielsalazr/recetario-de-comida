from django.contrib import admin
from .models import (
    Recipe,
    Category,
    ImageRecipe,
    CombinedRecipes,
)
# from picking.models import Dimension, Company, WarehouseCustomer, CollectionIndicator
# Register your models here.

# Register your models here.
""" class DocumentsAdmin(admin.ModelAdmin):
    form = Ingreso_Activo """

# PARAMETRIZACIONES
# admin.site.register(Dimension)
admin.site.register(Category)
admin.site.register(ImageRecipe)
admin.site.register(CombinedRecipes)



@admin.register(Recipe)
class ReciperAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        # 'categories',
    )
#     ordering = ('-date_created',)
#     search_fields = ('code', 'name')



