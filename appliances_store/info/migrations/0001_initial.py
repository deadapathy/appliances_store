# Generated by Django 4.0.2 on 2022-02-09 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=20)),
                ('surname', models.TextField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('telephone', models.IntegerField(max_length=8)),
                ('password', models.TextField(max_length=10)),
            ],
        ),
    ]
