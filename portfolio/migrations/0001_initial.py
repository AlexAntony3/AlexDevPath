# Generated by Django 3.2.20 on 2023-07-09 16:59

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('second_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('first_name', models.CharField(max_length=80, unique=True)),
                ('last_name', models.CharField(max_length=80, unique=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('nationality', models.CharField(max_length=200)),
                ('languages', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=400, unique=True)),
                ('freelance', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(max_length=200)),
                ('qualification', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=300)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('main_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('name_header', models.CharField(max_length=100)),
                ('intro_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('proficiency', models.IntegerField()),
                ('icon', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('thumbnail', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('description', models.TextField()),
                ('live_url', models.URLField()),
                ('github_URL', models.URLField()),
                ('skills', models.ManyToManyField(to='portfolio.Skill')),
            ],
        ),
    ]
