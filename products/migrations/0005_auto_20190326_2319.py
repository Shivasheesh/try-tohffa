# Generated by Django 2.1.7 on 2019-03-26 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20190325_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoframe',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='photoframe',
            unique_together={('title', 'slug')},
        ),
    ]
