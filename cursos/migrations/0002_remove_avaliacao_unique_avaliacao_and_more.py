# Generated by Django 5.1.1 on 2024-09-25 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='avaliacao',
            name='unique_avaliacao',
        ),
        migrations.RenameField(
            model_name='avaliacao',
            old_name='comunicacao',
            new_name='comentario',
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='criacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='criacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterUniqueTogether(
            name='avaliacao',
            unique_together={('email', 'curso')},
        ),
    ]
