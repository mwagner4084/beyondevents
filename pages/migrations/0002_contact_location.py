# Generated by Django 4.2.5 on 2023-10-02 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="location",
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
