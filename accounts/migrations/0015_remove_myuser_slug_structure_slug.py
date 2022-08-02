# Generated by Django 4.0.6 on 2022-07-31 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_myuser_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='slug',
        ),
        migrations.AddField(
            model_name='structure',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
