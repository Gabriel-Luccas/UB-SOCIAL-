from django.contrib import admin
from .models import Curso, Avaliacao

@admin.register(Curso)  # Registra o modelo Curso no Django Admin
class CursoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'url', 'criacao', 'atualizacao', 'ativo']
    search_fields = ['titulo', 'url']
    list_filter = ['ativo', 'criacao']
    ordering = ['titulo']

@admin.register(Avaliacao)  # Registra o modelo Avaliacao no Django Admin
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'curso', 'avaliacao', 'criacao', 'atualizacao', 'ativo']
    search_fields = ['nome', 'email', 'curso__titulo']
    list_filter = ['avaliacao', 'criacao', 'curso']
    ordering = ['nome']
