# Generated by Django 4.0.4 on 2022-05-01 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bulletins', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bulletin',
            options={'ordering': ['title'], 'verbose_name': 'Bulletin', 'verbose_name_plural': 'Bulletins'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
    ]
