from django.db import models
from django.db.models.deletion import DO_NOTHING
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Nombre en SAP")
    image = models.ImageField(upload_to='categories')

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        managed = True

    
    def __str__(self):
        return self.name


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Nombre receta")
    ingredients = models.TextField(verbose_name="ingredientes", blank=True, null=True)
    description = models.TextField(verbose_name="description", blank=True, null=True)
    categories = models.ManyToManyField(Category, verbose_name="categorias", blank=True, null=True, related_name="categories")
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=DO_NOTHING, blank=True, null=True, related_name="autor")

    class Meta:
        verbose_name_plural = "Recipes"
        managed = True

    
    def __str__(self):
        return self.name


class CombinedRecipes(models.Model):
    id = models.AutoField(primary_key=True)
    recipe1 = models.ForeignKey(Recipe, on_delete=DO_NOTHING, verbose_name="receta 1", blank=True, null=True, related_name="recipe1")
    recipe2 = models.ForeignKey(Recipe, on_delete=DO_NOTHING, verbose_name="receta 2", blank=True, null=True, related_name="recipe2")

    class Meta:
        verbose_name = "Receta Combinada"
        verbose_name_plural = "Recetas Combinadas"
        managed = True

    
    def __str__(self):
        return F"{self.recipe1} and {self.recipe2}" 

class ImageRecipe(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='recipes')
    recipe = models.ForeignKey(Recipe, on_delete=DO_NOTHING, verbose_name="Imagen Receta", blank=True, null=True)


    class Meta:
        verbose_name = "Image Recipe"
        verbose_name_plural = "Image Recipes"
        managed = True

    
    def __str__(self):
        return str(self.image)



# class CollectionIndicator(models.Model):
#     id = models.AutoField(primary_key=True)
#     code = models.CharField(max_length=5, verbose_name="Codigo En SAP")
#     name = models.CharField(max_length=255, verbose_name="Nombre en SAP")
#     date_created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

#     class Meta:
#         verbose_name = "Indicador Coleccion"
#         verbose_name_plural = "Indicador Colecciones"
#         managed = True

#     def __str__(self):
#         return self.name

# class Company(models.Model):
#     id = models.AutoField(primary_key=True, verbose_name="id")
#     name = models.CharField(default='', max_length=255, verbose_name="Nombre")

# class WarehouseCustomer(models.Model):
#     idWarehouseCustomer = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255, verbose_name="Nombre Bodega")
#     customer = models.CharField(max_length=255, verbose_name="Cliente")
    
#     class Meta:
#         verbose_name = "Almacene Cliente"
#         verbose_name_plural = "Almacenes Clientes"
#         managed = True

    
#     def __str__(self):
#         return self.name
    
# class Status(models.Model):
#     idStatus = models.AutoField(primary_key=True, verbose_name="id")
#     name = models.CharField(max_length=2, verbose_name="Nombre")

#     class Meta:
#         verbose_name = "Status"
#         verbose_name_plural = "Status"
#         managed = True

    
#     def __str__(self):
#         return self.name


# class DuplicatePickingRegister(models.Model):
#     id = models.AutoField(primary_key=True, verbose_name="id")
#     origin_picking = models.CharField(max_length=20,verbose_name="picking de origen")
#     destination_picking = models.CharField(max_length=20,verbose_name="picking de destino")
#     userCreated = models.CharField(max_length=255, verbose_name="Usuario Creador")
#     dateCreated = models.DateTimeField(verbose_name="Fecha Creación")
    



# class Picking(models.Model):
#     idPicking = models.AutoField(primary_key=True, verbose_name="id")
#     saleOrder = models.CharField(max_length=10, verbose_name="Orden Venta")
#     docTotalSaleOrder = models.IntegerField(verbose_name="Total Documento", blank=True, null=True)
#     customerCode = models.CharField(max_length=255, verbose_name="Codigo Cliente")
#     customerName = models.CharField(max_length=255, verbose_name="Codigo Cliente")
#     collection = models.CharField(max_length=255, verbose_name="Colección")
#     collectionId = models.CharField(max_length=5, verbose_name="Id Colección", blank=True, null=True)
#     comment = models.CharField(max_length=255, verbose_name="Comentario", blank=True, null=True)
#     userCreated = models.CharField(max_length=255, verbose_name="Usuario Creador")
#     dateCreated = models.DateTimeField(verbose_name="Fecha Creación")
#     userModified = models.CharField(max_length=255, verbose_name="Usuario Modificador")
#     dateModified = models.DateTimeField(verbose_name="Fecha Modificación")
#     status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, verbose_name="Estado")
#     company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, verbose_name="Compañia")
#     isDuplicated = models.BooleanField(default=False, verbose_name="esDuplicado", blank=True, null=True)
#     copiedDate = models.DateTimeField(default=None, verbose_name="Fecha copia", blank=True, null=True)
#     updateCopiedDate = models.DateTimeField(default=None, verbose_name="Fecha actualizacion copia", blank=True, null=True)
#     userCreatedCopy = models.CharField(max_length=30, verbose_name="Usuario Creador Copia", blank=True, null=True)
#     userUpdatedCopy = models.CharField(max_length=30, verbose_name="Usuario Actualizador Copia", blank=True, null=True)


#     class Meta:
#         verbose_name = "Picking"
#         verbose_name_plural = "Picking's"
#         managed = True


# class DuplicatedPicking(models.Model):
#     id = models.AutoField(primary_key=True, verbose_name="id")
#     idOrigen = models.ForeignKey(Picking, on_delete=models.DO_NOTHING, related_name='idOrigins')
#     idDestino = models.ForeignKey(Picking, on_delete=models.DO_NOTHING, related_name='idDestinations')


# class Dimension(models.Model):
#     idDimension = models.AutoField(primary_key=True, verbose_name="id")
#     name = models.CharField(max_length=100, verbose_name="Nombre")
#     dimension = models.CharField(max_length=255, verbose_name="Dimension", blank=True, null=True)
#     weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Peso", blank=True, null=True)

#     class Meta:
#         verbose_name = "Dimension"
#         verbose_name_plural = "Dimensiones"
#         managed = True

    
#     def __str__(self):
#         return self.name + " " + self.dimension

# class Box(models.Model):
#     idBox = models.AutoField(primary_key=True, verbose_name="id")
#     codebars = models.CharField(max_length=30, verbose_name="Codigo de Barras", unique=True)
#     comment = models.CharField(max_length=255, verbose_name="Comentarios", blank=True, null=True)
#     userCreated = models.CharField(max_length=255, verbose_name="Usuario Creador")
#     dateCreated = models.DateTimeField(verbose_name="Fecha de creacion")
#     userModified = models.CharField(max_length=255, verbose_name="Usuario Modificador")
#     dateModified = models.DateTimeField(verbose_name="Fecha de Modificación")
#     grossWeight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Bruto")
#     netWeight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Neto")
#     idDimension = models.ForeignKey(Dimension, on_delete=DO_NOTHING , verbose_name="Dimensión", blank=True, null=True)
#     idPicking = models.ForeignKey(Picking, on_delete=DO_NOTHING, verbose_name="Picking")
#     idWarehouseCustomer = models.ForeignKey(WarehouseCustomer, on_delete=DO_NOTHING, verbose_name="Bodega Cliente", blank=True, null=True)

#     class Meta:
#         verbose_name = "box"
#         verbose_name_plural = "boxes"
#         managed = True


# class BoxItem(models.Model):
#     idBoxItem = models.AutoField(primary_key=True, verbose_name="id")
#     codebars = models.CharField(max_length=30, verbose_name="Codigo de Barras")
#     itemCode = models.CharField(max_length=30, verbose_name="Codigo del Item")
#     price = models.IntegerField(verbose_name="Precio Item")
#     description = models.CharField(max_length=255, verbose_name="Descripcion") #-> Tabala OITM traerla
#     reference = models.CharField(max_length=30, verbose_name="Referencia")
#     color = models.CharField(max_length=255, verbose_name="Color")
#     size = models.CharField(max_length=5, verbose_name="Talla")
#     quantity = models.IntegerField(verbose_name="Cantidad")
#     userCreated = models.CharField(max_length=255, verbose_name="Usuario Creador")
#     dateCreated = models.DateTimeField(verbose_name="Fecha de Creación")
#     userModified = models.CharField(max_length=40, verbose_name="Usuario Modificador")
#     dateModified = models.DateTimeField(verbose_name="Fecha de Modificación")
#     idBox = models.ForeignKey(Box, on_delete=DO_NOTHING, verbose_name="Box")

#     class Meta:
#         verbose_name = "box Item"
#         verbose_name_plural = "Box Items"
#         managed = True
    
#     def __str__(self):
#         return self.itemCode




# class StatusHistory(models.Model):
#     id = models.AutoField(primary_key=True)
#     lastStatus = models.IntegerField(default=1, verbose_name="Status anterior")
#     status = models.ForeignKey(Status, verbose_name="status", on_delete=DO_NOTHING)
#     picking = models.ForeignKey(Picking, verbose_name="Picking", on_delete=DO_NOTHING)
#     change_state_date = models.DateTimeField(auto_now_add=timezone.now(), verbose_name="Fecha de cambio")

#     class Meta:
#         verbose_name = "Status History"
#         verbose_name_plural = "Status History"
#         managed = True