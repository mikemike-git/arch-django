# Generated by Django 4.2 on 2023-05-10 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0005_rename_question_choice_questionone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='questionone',
            new_name='question',
        ),
    ]
