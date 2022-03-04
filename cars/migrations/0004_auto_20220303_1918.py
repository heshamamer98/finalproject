# Generated by Django 3.2.12 on 2022-03-03 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0003_auto_20220303_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestCar',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carcolors', to='cars.carcolor', verbose_name='CarColors')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Requests', to=settings.AUTH_USER_MODEL, verbose_name='users')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Requests_Car',
        ),
    ]