# Generated by Django 3.0.7 on 2020-07-02 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0003_auto_20200702_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institutiontransactionmethod',
            name='image',
        ),
    ]
