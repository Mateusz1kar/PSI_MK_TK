# Generated by Django 2.2.7 on 2019-12-12 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stadoBaza', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='krowy',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='krowy', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
