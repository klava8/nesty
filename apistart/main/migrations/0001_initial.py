# Generated by Django 5.1.5 on 2025-01-20 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('desc', models.CharField(max_length=128, verbose_name='Описание')),
                ('completed', models.BooleanField(blank=True, null=True, verbose_name='Выполнен')),
            ],
        ),
    ]
