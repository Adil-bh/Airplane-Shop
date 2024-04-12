# Generated by Django 4.2.10 on 2024-04-12 13:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("airplane_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="id_client",
        ),
        migrations.RemoveField(
            model_name="orderdetail",
            name="id_order",
        ),
        migrations.RemoveField(
            model_name="orderdetail",
            name="id_product",
        ),
        migrations.DeleteModel(
            name="Customer",
        ),
        migrations.DeleteModel(
            name="Order",
        ),
        migrations.DeleteModel(
            name="OrderDetail",
        ),
        migrations.DeleteModel(
            name="Product",
        ),
    ]