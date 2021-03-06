# Generated by Django 3.1.4 on 2021-01-03 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('name', models.CharField(max_length=512, verbose_name='Название задачи')),
                ('start_date', models.DateTimeField(null=True, verbose_name='Дата создания')),
                ('end_date', models.DateTimeField(null=True, verbose_name='Дата создания')),
                ('success', models.BooleanField(null=True, verbose_name='Задача выполнена')),
            ],
        ),
    ]
