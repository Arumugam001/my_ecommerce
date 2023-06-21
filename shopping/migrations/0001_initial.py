# Generated by Django 4.0.3 on 2022-06-27 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product_section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Product_images/img')),
                ('cart', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('rating', models.CharField(max_length=48, verbose_name='fa fa-star')),
            ],
        ),
    ]
