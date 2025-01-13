# Generated by Django 5.0.2 on 2024-03-25 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0043_alter_charitypayment_giftcardcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charitypayment',
            name='giftcardcode',
            field=models.IntegerField(default='n/a', max_length=100),
        ),
        migrations.AlterField(
            model_name='charitypayment',
            name='giftcardimg',
            field=models.ImageField(blank=True, upload_to='photos/%y'),
        ),
        migrations.AlterField(
            model_name='charitypayment',
            name='giftcardname',
            field=models.CharField(default='n/a', max_length=100),
        ),
        migrations.AlterField(
            model_name='charitypayment',
            name='plan',
            field=models.CharField(default='n/a', max_length=100),
        ),
    ]