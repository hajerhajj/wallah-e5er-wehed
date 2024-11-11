# Generated by Django 5.0.4 on 2024-08-05 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashApp', '0006_remove_tn1apn_flyboxprotn1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='int',
            name='date',
            field=models.DateField(default='', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='soapn',
            name='date',
            field=models.DateField(default='', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='soepg',
            name='date',
            field=models.DateField(default='', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='somme',
            name='date',
            field=models.DateField(default='', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='tn1apn',
            name='date',
            field=models.DateField(default='', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='tn1epg',
            name='date',
            field=models.DateField(default='', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='tn1mme',
            name='date',
            field=models.DateField(default='', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='tn2apn',
            name='date',
            field=models.DateField(default='', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='tn2mme',
            name='date',
            field=models.DateField(default='', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='tn2vepg',
            name='date',
            field=models.DateField(default='', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='tn2vepgapn',
            name='date',
            field=models.DateField(default='', max_length=150, unique=True),
        ),
    ]
