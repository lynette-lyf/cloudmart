# Generated by Django 2.2.4 on 2019-11-13 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_lineitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitem',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]