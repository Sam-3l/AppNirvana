# Generated by Django 4.1.7 on 2023-04-18 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_artists_coverphoto_alter_artists_pp_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artists',
            old_name='story',
            new_name='media_post',
        ),
        migrations.AddField(
            model_name='artists',
            name='text_post',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='artists',
            name='coverphoto',
            field=models.FileField(null=True, upload_to='members/static/cover photos'),
        ),
        migrations.AlterField(
            model_name='artists',
            name='pp',
            field=models.FileField(null=True, upload_to='members/static/profile pics'),
        ),
    ]
