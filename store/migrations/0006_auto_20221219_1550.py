# Generated by Django 4.1.4 on 2022-12-19 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_second_name_customer_last_name'),
    ]

    operations = [
        migrations.RunSQL("""
        INSERT INTO store_collection(title)
        VALUES('collection1')
        ""","""
            DELETE FROM store_collection
            WHERE title='collection1'
            """)
    ]