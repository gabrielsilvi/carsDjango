# Generated by Django 4.2.7 on 2023-12-16 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_brand_alter_car_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, null='True', upload_to='cars/'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='car',
            name='plate',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]