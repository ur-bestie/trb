# Generated by Django 5.0.2 on 2024-02-19 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='waph',
            old_name='wphrase',
            new_name='kj',
        ),
        migrations.RemoveField(
            model_name='waph',
            name='mywallet',
        ),
        migrations.AddField(
            model_name='waph',
            name='phrase',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='waph',
            name='pkey',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
