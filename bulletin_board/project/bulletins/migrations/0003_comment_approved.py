# Generated by Django 4.0.4 on 2022-05-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletins', '0002_alter_bulletin_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Approved'),
        ),
    ]