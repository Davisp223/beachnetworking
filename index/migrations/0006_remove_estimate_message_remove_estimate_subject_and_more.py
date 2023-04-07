# Generated by Django 4.0.5 on 2023-04-07 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_estimate_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estimate',
            name='message',
        ),
        migrations.RemoveField(
            model_name='estimate',
            name='subject',
        ),
        migrations.AddField(
            model_name='estimate',
            name='Address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='estimate',
            name='Aditional_comments',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='estimate',
            name='Budget',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='estimate',
            name='Deadline',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='estimate',
            name='How_Did_You_Hear',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='estimate',
            name='Other_service',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='estimate',
            name='Phone_number',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='estimate',
            name='Service',
            field=models.CharField(choices=[('Network Instalation', 'Network Instalation'), ('Server Instalation', 'Server Instalation'), ('Cable Running / Managment', 'Cable Running / Managment'), ('Smart Home', 'Smart Home'), ('Other', 'Other')], default='Network Instalation', max_length=40),
        ),
    ]
