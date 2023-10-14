# Generated by Django 4.2.1 on 2023-10-09 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagestore', '0016_alter_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('cart', 'Cart'), ('processing', 'Processing'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='cart', max_length=20),
        ),
    ]
