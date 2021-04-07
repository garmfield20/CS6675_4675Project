# Generated by Django 3.1.7 on 2021-04-06 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('physicians', '0003_auto_20210406_1553'),
        ('distributors', '0009_auto_20210406_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributors',
            name='physicians',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='physicians.physicians'),
        ),
    ]
