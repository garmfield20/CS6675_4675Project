# Generated by Django 3.1.7 on 2021-04-15 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_auto_20210415_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='patient',
            field=models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='user.patient'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='physician',
            field=models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='user.physician'),
        ),
    ]
