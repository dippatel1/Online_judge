# Generated by Django 4.0.5 on 2022-07-13 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oj', '0004_alter_submissions_submission_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissions',
            name='submission_date',
            field=models.DateTimeField(),
        ),
    ]
