# Generated by Django 5.0.2 on 2024-03-25 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0044_alter_charitypayment_giftcardcode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charitypayment',
            name='giftcardcode',
            field=models.CharField(default='n/a', max_length=100),
        ),
    ]