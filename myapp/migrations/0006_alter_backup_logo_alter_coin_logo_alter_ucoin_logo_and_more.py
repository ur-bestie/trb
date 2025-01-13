# Generated by Django 5.0.2 on 2024-02-15 16:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_backup'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='backup',
            name='logo',
            field=models.ImageField(upload_to='logo/%y'),
        ),
        migrations.AlterField(
            model_name='coin',
            name='logo',
            field=models.ImageField(upload_to='logo/%y'),
        ),
        migrations.AlterField(
            model_name='ucoin',
            name='logo',
            field=models.ImageField(upload_to='logo/%y'),
        ),
        migrations.CreateModel(
            name='depht',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ucoin')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]