# Generated by Django 3.1.3 on 2021-01-10 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20201203_0736'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='meditation',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to='main_app.meditation'),
        ),
    ]