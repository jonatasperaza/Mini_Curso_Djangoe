from django.contrib import admin

# Register your models here.
from .models import Categoria, Produto
# from .models import Categoria

admin.site.register(Categoria)
admin.site.register(Produto)
# admin.site.register(Categoria)
