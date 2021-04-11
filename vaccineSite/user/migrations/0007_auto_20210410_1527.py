# Generated by Django 3.1.7 on 2021-04-10 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20210410_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='priority',
            field=models.CharField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')], default=None, max_length=256),
        ),
    ]
