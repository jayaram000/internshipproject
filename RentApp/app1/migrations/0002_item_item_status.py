# Generated by Django 5.0.2 on 2024-03-03 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_status',
            field=models.CharField(default='available', max_length=20),
        ),
    ]
