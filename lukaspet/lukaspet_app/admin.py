from django.contrib import admin
from .models import Categoria, Marca, Producto, CarritoCompra, ItemCarrito
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(CarritoCompra)
admin.site.register(ItemCarrito)