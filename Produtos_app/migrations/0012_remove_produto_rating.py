# Generated by Django 4.1.2 on 2022-10-17 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Produtos_app', '0011_alter_produto_publicado_por'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='rating',
        ),
    ]
