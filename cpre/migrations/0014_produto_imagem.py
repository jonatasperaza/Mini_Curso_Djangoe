# Generated by Django 5.0 on 2023-12-06 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpre', '0013_remove_produto_categoria_produto_categorias'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='produtos/'),
        ),
    ]
