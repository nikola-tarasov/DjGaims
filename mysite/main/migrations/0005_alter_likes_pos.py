# Generated by Django 4.2.2 on 2023-07-30 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='pos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.gaim', verbose_name='commentslike'),
        ),
    ]
