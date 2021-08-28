# Generated by Django 3.2.6 on 2021-08-17 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=225, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('video_id', models.CharField(max_length=225)),
            ],
            options={
                'verbose_name': 'Movie Video',
                'verbose_name_plural': 'Netflix Videos',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='VideoProxy',
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=225)),
                ("slug", models.SlugField(blank=True)),
            ],
            options={
                'verbose_name': 'Movie Video',
                'verbose_name_plural': 'Basic Video Title Show',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('video.video',),
        ),
    ]
