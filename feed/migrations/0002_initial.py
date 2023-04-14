# Generated by Django 4.2 on 2023-04-14 05:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('board', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feedmodel',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.post'),
        ),
    ]