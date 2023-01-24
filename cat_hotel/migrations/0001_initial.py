# Generated by Django 4.1 on 2023-01-24 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(max_length=200, null=True)),
                ("email", models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "number_room",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("description", models.TextField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Booking",
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
                ("description", models.TextField(max_length=200, null=True)),
                ("start_date", models.DateField(auto_now_add=True, null=True)),
                ("start_time", models.TimeField(auto_now_add=True, null=True)),
                ("end_date", models.DateField(auto_now_add=True, null=True)),
                ("end_time", models.TimeField(auto_now_add=True, null=True)),
                ("cat", models.TextField(max_length=200, null=True)),
                ("phone_number", models.TextField(max_length=200, null=True)),
                (
                    "room_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cat_hotel.room"
                    ),
                ),
            ],
        ),
    ]
