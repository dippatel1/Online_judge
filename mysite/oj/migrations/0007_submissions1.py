# Generated by Django 4.0.5 on 2022-07-13 05:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oj', '0006_alter_submissions_submission_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='submissions1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Submission_verdict', models.CharField(default='unsolved', max_length=10)),
                ('submission_date', models.DateField()),
                ('submitted_code', models.TextField(default='', max_length=1000)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oj.question')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
