# Generated by Django 4.0.6 on 2022-08-01 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_rename_chiffre_structure_chiffres_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='structure',
            old_name='chiffres',
            new_name='compta',
        ),
    ]