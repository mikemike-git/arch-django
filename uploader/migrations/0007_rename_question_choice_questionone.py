# Generated by Django 4.2 on 2023-05-10 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0006_rename_questionone_choice_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='questionone',
        ),
    ]