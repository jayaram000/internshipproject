# Generated by Django 5.0.2 on 2024-05-01 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_alter_bookingrequest_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingrequest',
            name='uploadedBy',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
