# Generated by Django 4.0.6 on 2022-09-02 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_myuser_groupe'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='permission',
            field=models.CharField(choices=[('Commercial', 'Commercial'), ('Partenaire', 'Partenaire'), ('Responsable', 'Responsable')], default='', max_length=15),
            preserve_default=False,
        ),
    ]