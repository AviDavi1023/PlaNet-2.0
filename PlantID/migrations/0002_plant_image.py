# Generated by Django 5.0.4 on 2024-06-16 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlantID', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
