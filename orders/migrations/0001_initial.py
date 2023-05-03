# Generated by Django 4.2 on 2023-05-03 13:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "order_status",
                    models.CharField(
                        choices=[
                            ("PEDIDO REALIZADO", "Order Started"),
                            ("EM ANDAMENTO", "Order In Progess"),
                            ("ENTREGUE", "Delivered"),
                        ],
                        default="PEDIDO REALIZADO",
                    ),
                ),
                (
                    "total_price",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["id"],
            },
        ),
    ]