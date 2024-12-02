# Generated by Django 5.1.3 on 2024-12-02 09:16

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='level',
            field=models.PositiveIntegerField(default='1', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='lft',
            field=models.PositiveIntegerField(default='2', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='rght',
            field=models.PositiveIntegerField(default='3', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default='1', editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='Product.category'),
        ),
    ]
