# Generated by Django 2.2.4 on 2020-08-26 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_english', models.CharField(max_length=100, null=True)),
                ('synonyms', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(max_length=10000)),
                ('image', models.ImageField(upload_to='movies')),
                ('type_show', models.CharField(choices=[('TV', 'TV'), ('MO', 'MOVIE')], max_length=2, null=True)),
                ('episodes', models.IntegerField(default=12)),
                ('category', models.CharField(choices=[('SC', 'SCHOOL'), ('PS', 'PSYCHOLOGICAL'), ('CO', 'COMEDY'), ('SE', 'SEINEN'), ('RO', 'ROMANCE')], max_length=2)),
                ('status', models.CharField(choices=[('RA', 'RECENTLY ADDED'), ('MW', 'MOST WATCHED'), ('TR', 'TOP RATED')], max_length=2)),
                ('year_of_production', models.IntegerField()),
                ('producers', models.CharField(max_length=50, null=True)),
                ('duration', models.IntegerField(default=25)),
                ('score', models.FloatField(default=0.0)),
                ('ranked', models.IntegerField(default=0)),
                ('views_count', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'animelist',
            },
        ),
    ]
