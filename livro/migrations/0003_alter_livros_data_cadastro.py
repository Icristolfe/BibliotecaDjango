# Generated by Django 4.2.4 on 2023-11-09 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0002_alter_livros_options_alter_livros_co_autor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='data_cadastro',
            field=models.DateField(auto_now=True),
        ),
    ]
