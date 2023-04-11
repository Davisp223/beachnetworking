# Generated by Django 4.1.6 on 2023-04-11 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_remove_estimate_message_remove_estimate_subject_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estimate',
            name='How_Did_You_Hear',
        ),
        migrations.AddField(
            model_name='estimate',
            name='How_Did_You_Hear_About_Us',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='estimate',
            name='prefered_contact_method',
            field=models.CharField(choices=[('Email', 'Email'), ('Phone', 'Phone')], default='Email', max_length=100),
        ),
        migrations.AlterField(
            model_name='estimate',
            name='Budget',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='estimate',
            name='Deadline',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='estimate',
            name='Other_service',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='company_name',
            field=models.CharField(max_length=30),
        ),
    ]