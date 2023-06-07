# Generated by Django 4.1.5 on 2023-06-06 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_producttags_tag_name_en_producttags_tag_name_ru'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='categories_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='categories_ru',
        ),
        migrations.AddField(
            model_name='productcategory',
            name='category_en',
            field=models.CharField(max_length=30, null=True, verbose_name='Product category'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='category_ru',
            field=models.CharField(max_length=30, null=True, verbose_name='Product category'),
        ),
    ]