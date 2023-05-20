# Generated by Django 4.1.5 on 2023-05-04 14:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_categories'),
        ('users', '0004_userreview_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userreview',
            old_name='coment',
            new_name='comment',
        ),
        migrations.AlterField(
            model_name='userreview',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to='shop.product'),
        ),
    ]