# Generated by Django 3.1.7 on 2021-04-06 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('physicians', '0002_auto_20210406_1455'),
        ('distributors', '0006_auto_20210406_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributors',
            name='physicians',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='physicians.physicians'),
        ),
    ]
