# Generated by Django 5.0 on 2023-12-06 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpre', '0012_delete_categorias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='categoria',
        ),
        migrations.AddField(
            model_name='produto',
            name='categorias',
            field=models.ManyToManyField(to='cpre.categoria'),
        ),
    ]
