# Generated by Django 5.1.6 on 2025-02-16 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glovo', '0002_alter_courierrating_rating_alter_order_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_name_en',
            field=models.CharField(max_length=54, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_ru',
            field=models.CharField(max_length=54, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_name_en',
            field=models.CharField(max_length=54, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_name_ru',
            field=models.CharField(max_length=54, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='address_en',
            field=models.CharField(max_length=98, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='address_ru',
            field=models.CharField(max_length=98, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='description_ru',
            field=models.TextField(null=True),
        ),
    ]
