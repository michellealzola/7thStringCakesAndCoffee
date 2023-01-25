# Generated by Django 4.1.4 on 2022-12-29 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_subproduct_subproduct_shop_subpro_id_2b8819_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subproduct',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='subproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.product'),
        ),
    ]
