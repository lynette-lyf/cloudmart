# Generated by Django 2.2.7 on 2019-11-20 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_product_origin'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ingredients',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]