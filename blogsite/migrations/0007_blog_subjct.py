# Generated by Django 2.2.7 on 2021-07-14 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0006_auto_20210714_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='subjct',
            field=models.CharField(default='Null', max_length=20),
        ),
    ]
