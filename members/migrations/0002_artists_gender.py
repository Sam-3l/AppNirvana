# Generated by Django 4.1.7 on 2023-04-11 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artists',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
