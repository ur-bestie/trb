# Generated by Django 5.0.2 on 2024-03-25 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0042_alter_charitypayment_giftcardcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charitypayment',
            name='giftcardcode',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]