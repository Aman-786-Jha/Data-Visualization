# Generated by Django 4.1.5 on 2023-01-15 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualize2', '0002_datadata_added_datadata_country_datadata_impact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datadata',
            name='sector',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
