# Generated by Django 5.1.5 on 2025-02-02 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cases',
            options={'verbose_name': 'Case', 'verbose_name_plural': 'Cases'},
        ),
        migrations.AlterModelOptions(
            name='items',
            options={'verbose_name': 'Item', 'verbose_name_plural': 'Items'},
        ),
        migrations.AddField(
            model_name='cases',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/case_image/'),
        ),
        migrations.AddField(
            model_name='items',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/item_image/'),
        ),
        migrations.AlterField(
            model_name='items',
            name='rarity',
            field=models.CharField(choices=[('Ordinary', 'Ordinary'), ('Rare', 'Rare'), ('Epic', 'Epic'), ('Mythical', 'Mythical'), ('Legendary', 'Legendary')], max_length=50),
        ),
    ]
