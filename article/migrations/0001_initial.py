# Generated by Django 5.1.1 on 2024-09-18 06:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=300, unique=True)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=200)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('article_cost', models.FloatField(default=0.0)),
                ('article_category', models.CharField(choices=[('programming', 'programming'), ('News', 'News'), ('IT', 'IT'), ('Science', 'Science'), ('Health', 'Health')], max_length=50)),
            ],
        ),
    ]