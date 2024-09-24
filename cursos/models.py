from django.db import models

# Create your models here.

class Base(models.Model):
    criacao = models.DateField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Curso(Base):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"  # Corrigido "veebose_names_plural"

    def __str__(self):
        return self.titulo


class Avaliacao(Base):
    curso = models.ForeignKey(
        Curso, related_name="avaliacoes", on_delete=models.CASCADE  # Corrigido o plural de "avaliacoes"
    )
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comunicacao = models.TextField(blank=True, default="")
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = "Avaliação"  # Corrigido "Avaliaçoe"
        verbose_name_plural = "Avaliações"  # Corrigido o plural
        constraints = [  # Novo método recomendado no Django 2.2+
            models.UniqueConstraint(fields=['email', 'curso'], name='unique_avaliacao')
        ]

    def __str__(self):
        return f"{self.nome} avaliou o curso {self.curso} com a nota de {self.avaliacao}"
