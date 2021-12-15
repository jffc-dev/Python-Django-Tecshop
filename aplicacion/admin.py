from django.contrib import admin
from .models import Categoria, Subcategoria, Producto, Deseo, Compra, Comentario, Usuario, Imagen, DetalleCompra
class ImagenInline(admin.StackedInline):
    model = Imagen
    extra = 2
    min_num= 1
    max_num = 5
class DetalleCompraInline(admin.TabularInline):
    model = DetalleCompra
    extra = 2
    min_num = 1
class SubcategoriaInline(admin.TabularInline):
    model = Subcategoria
    extra = 2
    min_num = 1
class CategoriaAdmin(admin.ModelAdmin):
    inlines=[SubcategoriaInline,]
class ProductoAdmin(admin.ModelAdmin):
    inlines = [ImagenInline, ]
class CompraAdmin(admin.ModelAdmin):
    inlines = [DetalleCompraInline, ]
# Register your models here.
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Deseo)
admin.site.register(Compra,CompraAdmin)
admin.site.register(Usuario)
admin.site.register(Producto,ProductoAdmin)

#auth
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']
