# Generated by Django 4.2.7 on 2024-07-26 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_cariventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
