# Generated by Django 3.1.5 on 2021-02-08 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0003_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='full_name',
            field=models.CharField(default=23, max_length=50),
            preserve_default=False,
        ),
    ]