# Generated by Django 4.2 on 2023-04-13 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0001_initial'),
        ('board', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feedmodel',
            name='feed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.post'),
        ),
    ]
