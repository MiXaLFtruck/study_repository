# Generated by Django 4.0.5 on 2022-07-01 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0002_alter_appuser_options_room_is_direct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='users',
            field=models.ManyToManyField(to='messenger.appuser'),
        ),
    ]
