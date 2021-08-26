# Generated by Django 3.2.6 on 2021-08-25 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("playlist", "0003_auto_20210825_0958"),
        ("video", "0028_alter_video_playlist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="playlist",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="video",
                to="playlist.playlist",
                verbose_name="Playlist",
            ),
        ),
    ]
