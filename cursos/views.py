from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework import mixins, viewsets
from rest_framework import permissions
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):

    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = CursoSerializer(data=data.request)
        data.is_valid(raise_exception=True)
        data.save()
        return Response(data.data, status=status.HTTP_201_CREATED)


class AvaliacaoAPIView(APIView):

    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = AvaliacaoSerializer(data=data.request)
        data.is_valid(raise_exception=True)
        data.save()
        return Response(data.data, status=status.HTTP_201_CREATED)


# Plural options for Curso
class PluralCursosAPIGeneric(generics.ListAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


# Singular options for Curso
class SingularCursoAPIGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


# Plural options for Avaliacao
class PluralAvaliacosAPIGenerics(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get("curso_pk"):
            return self.queryset.filter(curso_id=self.kwargs.get("curso_pk"))
        return self.queryset.all()


# Singular options for CAvaliacao
class SingularAvaliacaoAPIGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_objects(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get('curso_pk'), pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


# API v2
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        curso = self.get_object()
        serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        return Response(serializer.data)

''' ViewSet padrão
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
'''

# ViewSet customizada (Retirado o 'mixins.ListModelMixin')
class AvaliacaoViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer