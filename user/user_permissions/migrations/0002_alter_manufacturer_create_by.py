# Generated by Django 4.1.7 on 2023-03-03 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_permissions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='create_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creat', to=settings.AUTH_USER_MODEL),
        ),
    ]