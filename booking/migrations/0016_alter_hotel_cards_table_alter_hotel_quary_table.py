# Generated by Django 5.0.3 on 2024-03-21 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0015_rename_faqitem_hotel_faqitem_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='hotel_cards',
            table='hotel_cards',
        ),
        migrations.AlterModelTable(
            name='hotel_quary',
            table='hotel_quary',
        ),
    ]
