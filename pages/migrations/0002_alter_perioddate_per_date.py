# Generated by Django 4.0.2 on 2022-04-14 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perioddate',
            name='per_date',
            field=models.CharField(max_length=15),
        ),
    ]