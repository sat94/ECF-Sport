# Generated by Django 4.0.6 on 2022-09-23 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_myuser_photo_alter_partenaire_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo'),
        ),
        migrations.AlterField(
            model_name='partenaire',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='ville'),
        ),
        migrations.AlterField(
            model_name='structure',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='salle'),
        ),
    ]