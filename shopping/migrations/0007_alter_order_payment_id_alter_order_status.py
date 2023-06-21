# Generated by Django 4.0.3 on 2022-07-17 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0006_order_profile_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_id',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Out For Shopping', 'Out For Shipping'), ('Pending', 'Pending')], default='Pending', max_length=150),
        ),
    ]