# Generated by Django 3.1.7 on 2021-04-14 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20210414_1513'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='appointment',
            name='name of constraint',
        ),
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together={('currphysician', 'patient', 'vaccineName')},
        ),
    ]
