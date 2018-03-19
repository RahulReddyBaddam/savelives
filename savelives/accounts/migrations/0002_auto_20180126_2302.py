# Generated by Django 2.0 on 2018-01-26 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Brand', 'verbose_name_plural': 'Brands'},
        ),
        migrations.AlterField(
            model_name='medicine',
            name='company',
            field=models.ManyToManyField(related_name='brand', to='accounts.Brand'),
        ),
        migrations.AlterField(
            model_name='pharma',
            name='meds',
            field=models.ManyToManyField(related_name='meds', to='accounts.Medicine'),
        ),
    ]
