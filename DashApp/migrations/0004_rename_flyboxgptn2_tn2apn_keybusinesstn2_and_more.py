# Generated by Django 5.0.4 on 2024-07-31 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DashApp', '0003_soapn_tn1apn_tn2apn_tn2vepgapn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tn2apn',
            old_name='flyboxgptn2',
            new_name='keybusinesstn2',
        ),
        migrations.RenameField(
            model_name='tn2vepgapn',
            old_name='flyboxprotn2vepg',
            new_name='flyboxgptn2vepg',
        ),
        migrations.RemoveField(
            model_name='soapn',
            name='keyproso',
        ),
        migrations.RemoveField(
            model_name='tn1apn',
            name='flyboxgptn1',
        ),
    ]
