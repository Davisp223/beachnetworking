# Generated by Django 4.0.5 on 2023-04-06 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_estimate_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='bio',
            new_name='company_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
    ]
