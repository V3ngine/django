# Generated by Django 4.1.5 on 2023-03-23 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('max', '0010_alter_category_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='category', verbose_name='Фото'),
        ),
    ]