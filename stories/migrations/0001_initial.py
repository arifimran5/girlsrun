# Generated by Django 3.0.8 on 2020-08-18 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('occupation', models.CharField(max_length=254)),
                ('details', models.TextField(default='some string')),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Stories',
            },
        ),
    ]