from django.contrib import admin

# Register your models here.
from .models import Categoria, Pais, tipoatuacao, Produtora, Membros, Filme, Atuacao

admin.site.register(Categoria)
admin.site.register(Pais)
admin.site.register(tipoatuacao)
admin.site.register(Produtora)
admin.site.register(Membros)
admin.site.register(Filme)
admin.site.register(Atuacao)