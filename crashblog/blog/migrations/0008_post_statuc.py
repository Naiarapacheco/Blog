# Generated by Django 5.0.4 on 2024-04-22 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_post_posts_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='statuc',
            field=models.CharField(choices=[('active', 'Active'), ('draft', 'Draft')], default='active', max_length=10),
        ),
    ]
