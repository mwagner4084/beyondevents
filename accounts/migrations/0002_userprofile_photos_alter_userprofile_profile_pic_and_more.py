# Generated by Django 5.0 on 2024-01-30 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='photos',
            field=models.ImageField(blank=True, null=True, upload_to='user_photos'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='user_photos'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='wedding_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
