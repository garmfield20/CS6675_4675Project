# Generated by Django 3.1.7 on 2021-03-31 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccine',
            name='vaccine_id',
            field=models.CharField(max_length=256),
        ),
    ]