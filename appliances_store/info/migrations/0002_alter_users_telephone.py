# Generated by Django 4.0.2 on 2022-02-16 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='telephone',
            field=models.IntegerField(),
        ),
    ]
