# Generated by Django 5.0.6 on 2024-05-27 17:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='default_shipping_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_query_name='user_info', to='ecom.shippingaddress'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipping_addresses', to='ecom.user'),
        ),
    ]
