# Generated by Django 4.0.1 on 2022-02-06 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('computers', 'Computers'), ('house', 'House and Garden'), ('clothing', 'Clothing'), ('car', 'Car Products'), ('toys', 'Toys')], default=1, max_length=30),
        ),
    ]
