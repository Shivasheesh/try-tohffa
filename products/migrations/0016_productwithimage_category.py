# Generated by Django 2.1.7 on 2019-03-31 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20190331_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='productwithimage',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='products.Producttype'),
            preserve_default=False,
        ),
    ]
