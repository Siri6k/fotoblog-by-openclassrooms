# Generated by Django 4.1.3 on 2022-11-13 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='date_cteated',
            new_name='date_created',
        ),
    ]
