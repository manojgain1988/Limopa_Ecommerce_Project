# Generated by Django 5.1.3 on 2024-11-28 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('keyword', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField()),
                ('phone', models.IntegerField()),
                ('fax', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('smptserver', models.CharField(blank=True, max_length=100, null=True)),
                ('smtpemail', models.EmailField(blank=True, max_length=50, null=True)),
                ('smptpassword', models.CharField(blank=True, max_length=50, null=True)),
                ('smptport', models.CharField(blank=True, max_length=100, null=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icon/')),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('contact', models.TextField(blank=True, null=True)),
                ('reference', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
