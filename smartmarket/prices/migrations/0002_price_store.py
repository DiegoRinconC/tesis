# Generated by Django 2.1.2 on 2018-10-23 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shops', '0001_initial'),
        ('prices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shops.Shop'),
        ),
    ]
