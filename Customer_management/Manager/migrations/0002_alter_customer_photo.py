# Generated by Django 3.2.9 on 2021-11-17 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='photo',
            field=models.ImageField(blank=True, default='alternative.jpg', null=True, upload_to=''),
        ),
    ]
