# Generated by Django 4.0.1 on 2022-04-29 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField(max_length=50)),
                ('image', models.ImageField(default='', upload_to='')),
                ('demo', models.URLField(default='')),
                ('download', models.URLField(default='')),
            ],
        ),
    ]
