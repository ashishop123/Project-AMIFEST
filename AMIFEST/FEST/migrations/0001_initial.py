# Generated by Django 3.1.3 on 2021-03-02 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122, verbose_name='event name')),
                ('date', models.DateField(verbose_name='event date')),
                ('venue', models.CharField(max_length=120)),
                ('block', models.CharField(max_length=120, verbose_name='block name')),
                ('manager', models.CharField(max_length=120, verbose_name='manager name')),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
