# Generated by Django 4.2.11 on 2024-06-04 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='taskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=50)),
                ('taskDescription', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]