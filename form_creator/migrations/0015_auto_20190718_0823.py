# Generated by Django 2.2.3 on 2019-07-18 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_creator', '0014_auto_20190718_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfield',
            name='data_type',
            field=models.CharField(choices=[('TX', 'Text'), ('NUM', 'Number'), ('DAT', 'Date'), ('EML', 'Email')], max_length=3),
        ),
    ]
