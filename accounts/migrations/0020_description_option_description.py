# Generated by Django 4.0.6 on 2022-08-01 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_remove_option_accompagne_remove_option_assistance_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='option',
            name='description',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.description'),
        ),
    ]
