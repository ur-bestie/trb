# Generated by Django 5.0.2 on 2024-03-18 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0035_cardcreate_alter_settings_siteemail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardcreate',
            name='logo',
            field=models.ImageField(default=1, upload_to='photos/%y'),
            preserve_default=False,
        ),
    ]