# Generated by Django 3.1.7 on 2021-04-15 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_auto_20210415_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]