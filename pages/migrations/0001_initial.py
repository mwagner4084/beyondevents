# Generated by Django 4.2.5 on 2023-10-01 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("fname", models.CharField(blank=True, max_length=254, null=True)),
                ("lname", models.CharField(blank=True, max_length=254, null=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone", models.CharField(blank=True, max_length=254, null=True)),
                ("wedding_date", models.DateField(auto_now_add=True)),
                ("comments", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "referred_by",
                    models.CharField(blank=True, max_length=254, null=True),
                ),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("contacted", models.BooleanField(default=False)),
                ("notes", models.CharField(blank=True, max_length=5000, null=True)),
            ],
        ),
    ]
