from django.contrib import admin
from .models import Login, Cliente, Contacto, Marca, Producto


admin.site.register(Login)
admin.site.register(Cliente)
admin.site.register(Contacto)
admin.site.register(Marca)
admin.site.register(Producto)