# Generated by Django 2.2.3 on 2019-07-17 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_creator', '0009_userform_submissions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userform',
            old_name='submissions',
            new_name='submissions_counter',
        ),
    ]
