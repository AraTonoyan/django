# Generated by Django 4.1.5 on 2023-02-04 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_shortabout_button'),
    ]

    operations = [
        migrations.AddField(
            model_name='calltoaction',
            name='button',
            field=models.CharField(default=1, max_length=25, verbose_name='Button text'),
            preserve_default=False,
        ),
    ]
