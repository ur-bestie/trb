# Generated by Django 5.0.2 on 2024-03-27 00:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0053_giftcardpay_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='charitypayment',
            name='charity',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.charity'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='giftcardpay',
            name='charity',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.charity'),
            preserve_default=False,
        ),
    ]
