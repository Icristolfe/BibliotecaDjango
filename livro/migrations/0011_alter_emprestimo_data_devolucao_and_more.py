# Generated by Django 4.2.4 on 2024-01-03 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0010_emprestimo_nome_emprestado_anonimo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_devolucao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(blank=True, null=True),
        ),
    ]
