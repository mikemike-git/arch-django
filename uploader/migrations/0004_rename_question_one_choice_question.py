# Generated by Django 4.2 on 2023-05-10 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0003_rename_question_choice_question_one'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question_one',
            new_name='question',
        ),
    ]
