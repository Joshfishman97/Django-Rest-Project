# Generated by Django 3.2.8 on 2021-10-20 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drfapp', '0003_student_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='description',
            field=models.TextField(default=None, null=True),
        ),
    ]
