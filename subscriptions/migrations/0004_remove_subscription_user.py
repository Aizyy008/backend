# Generated by Django 4.2.20 on 2025-03-16 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_usersubscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='user',
        ),
    ]
