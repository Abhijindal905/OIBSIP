# Generated by Django 5.0.6 on 2024-11-18 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_remove_student_email_remove_student_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
