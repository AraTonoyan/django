# Generated by Django 4.1.5 on 2023-02-04 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_calltoaction_button_shortabout_button'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calltoaction',
            name='button',
        ),
        migrations.RemoveField(
            model_name='shortabout',
            name='button',
        ),
    ]
