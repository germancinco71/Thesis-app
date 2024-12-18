# Generated by Django 5.1.3 on 2024-12-08 16:35

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='object_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='thesis.medpapers'),
        ),
        migrations.CreateModel(
            name='itcomment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='thesis.itpapers')),
            ],
        ),
    ]
