# Generated by Django 4.1.5 on 2023-02-05 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_productpagehead'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPageHead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redTitle', models.CharField(max_length=30, verbose_name='First Title')),
                ('whiteTitle', models.CharField(max_length=30, verbose_name='Second Title')),
            ],
        ),
    ]
