# Generated by Django 4.2.3 on 2023-07-20 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_category_subcategory_parent_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='parent_category',
            new_name='category',
        ),
        migrations.AddField(
            model_name='country',
            name='parent_country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='posts.country'),
        ),
    ]
