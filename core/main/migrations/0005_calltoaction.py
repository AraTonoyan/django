# Generated by Django 4.1.5 on 2023-02-04 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_shortabout'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallToAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35, verbose_name='Main title')),
                ('text', models.CharField(max_length=120, verbose_name='short about')),
            ],
        ),
    ]