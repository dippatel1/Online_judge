# Generated by Django 4.0.5 on 2022-07-13 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oj', '0005_alter_submissions_submission_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissions',
            name='submission_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='submissions',
            name='submitted_code',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
