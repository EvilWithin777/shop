# Generated by Django 4.2.1 on 2023-10-06 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagestore', '0011_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
