# Generated by Django 3.2.9 on 2023-03-12 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('park_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ivent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ivetn_id', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='photos')),
                ('title', models.TextField()),
                ('data_start', models.DateField()),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='park_user.author')),
            ],
        ),
        migrations.CreateModel(
            name='Creater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('activity', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('instagram', models.CharField(blank=True, max_length=50, null=True)),
                ('telegram', models.CharField(blank=True, max_length=50, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=50, null=True)),
                ('gmail', models.CharField(blank=True, max_length=30, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creater', to='park_user.author')),
            ],
        ),
    ]
