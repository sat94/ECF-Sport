# Generated by Django 4.0.6 on 2022-09-02 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_myuser_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partenaire',
            name='numberPhone',
            field=models.IntegerField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='structure',
            name='numberPhone',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
