# Generated by Django 5.0.6 on 2024-05-24 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaryproduct',
            name='expiry_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
