# Generated by Django 4.1.7 on 2023-04-12 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_artists_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artists',
            name='coverphoto',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='artists',
            name='pp',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='artists',
            name='story',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
