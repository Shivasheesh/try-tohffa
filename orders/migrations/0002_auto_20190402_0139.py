# Generated by Django 2.1.7 on 2019-04-01 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
