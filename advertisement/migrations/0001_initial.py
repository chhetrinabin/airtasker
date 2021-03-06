# Generated by Django 3.1.3 on 2020-11-27 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ads_title', models.CharField(max_length=255, null=True)),
                ('ads_slug', models.SlugField(unique=True)),
                ('ads_description', models.TextField()),
                ('room_size', models.CharField(choices=[('', 'Select room size'), ('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], default='', max_length=6)),
                ('no_of_rooms_available', models.PositiveIntegerField(null=True)),
                ('date_of_availability', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('suburb', models.CharField(max_length=100, null=True)),
                ('nearby_landmark', models.CharField(max_length=100)),
                ('weekly_rent', models.PositiveIntegerField(null=True)),
                ('bond_amount_required', models.PositiveIntegerField(null=True)),
                ('ads_pictures', models.ImageField(upload_to='ads_images/% Y/% m/% d/')),
                ('ads_approval_status', models.BooleanField(default=False)),
                ('ads_status', models.CharField(choices=[('', 'Select ads status'), ('Inactive', 'Inactive'), ('Under-Review', 'Under-Review'), ('Active', 'Active')], default='', max_length=20)),
                ('ads_total_views', models.PositiveIntegerField(default=0)),
                ('ads_date_created', models.DateTimeField(auto_now_add=True)),
                ('ads_date_updated', models.DateTimeField(auto_now=True)),
                ('advertiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('reason', models.TextField()),
                ('advertisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisement.advertisement')),
                ('moderator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_Favourite', models.BooleanField(default=False)),
                ('advertisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisement.advertisement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
