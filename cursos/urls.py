from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)


urlpatterns = [
    path("cursos/", CursoAPIView.as_view(), name="cursos1"),
    path("avaliacoes/", AvaliacaoAPIView.as_view(), name="cursos1"),
    
    
    path("cursos/generic/cursos/", PluralCursosAPIGeneric.as_view(), name="cursos"),#http://127.0.0.1:8000/api/v1/cursos/generic/curso/1/
    path("cursos/generic/curso/<int:pk>/", SingularCursoAPIGeneric.as_view(), name="curso"),#http://127.0.0.1:8000/api/v1/cursos/generic/cursos/
    
    path("cursos/generic/curso/<int:curso_pk>/avaliacoes/", PluralAvaliacosAPIGenerics.as_view(), name="curso-avaliaçoes"),
    path("cursos/generic/curso/<int:curso_pk>/avaliacao/<int:avaliacao_pk>/", SingularAvaliacaoAPIGenerics.as_view(), name="curso-avaliaçao"),
    
    
    path("avaliacoes/generic/avaliacoes/", PluralAvaliacosAPIGenerics.as_view(), name="Avaliaçoes"),#http://127.0.0.1:8000/api/v1/avaliacoes/generic/avaliacoes/
    path("avaliacoes/generic/avaliacao/<int:pk>/",SingularAvaliacaoAPIGenerics.as_view(),name="Avaliaçao",),#http://127.0.0.1:8000/api/v1/avaliacoes/generic/avaliacao/1/
]
