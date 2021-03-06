# Generated by Django 3.2.12 on 2022-03-02 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requests_Car',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('mudel', models.IntegerField()),
                ('transmission', models.CharField(max_length=100)),
                ('engin_size', models.CharField(max_length=100)),
                ('powerBHP', models.CharField(max_length=100)),
                ('distance_meter', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests_cars', to=settings.AUTH_USER_MODEL, verbose_name='users')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
