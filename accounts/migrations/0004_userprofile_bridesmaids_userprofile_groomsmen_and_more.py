# Generated by Django 5.0 on 2024-01-30 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_first_name_customuser_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bridesmaids',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='groomsmen',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='guests',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
