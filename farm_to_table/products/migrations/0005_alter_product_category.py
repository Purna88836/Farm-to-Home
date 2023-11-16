# Generated by Django 4.2.6 on 2023-10-15 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_category_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('fruits', 'Fruits'), ('vegetables', 'Vegetables'), ('dairy products', 'Dairy Products'), ('grains', 'Grains')], max_length=50),
        ),
    ]