# Generated by Django 5.1.3 on 2024-11-28 09:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('keywords', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='product/')),
                ('new_price', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('amount', models.IntegerField(default=0)),
                ('min_amount', models.IntegerField(default=3)),
                ('detail', models.TextField()),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=20)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.category')),
            ],
        ),
    ]
