# Generated by Django 4.1.5 on 2023-01-15 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualize2', '0005_alter_datadata_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datadata',
            name='insight',
        ),
        migrations.AlterField(
            model_name='datadata',
            name='end_year',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datadata',
            name='id',
            field=models.TextField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='datadata',
            name='impact',
            field=models.TextField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='datadata',
            name='intensity',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datadata',
            name='likelihood',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datadata',
            name='pestle',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datadata',
            name='region',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datadata',
            name='relevance',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datadata',
            name='sector',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datadata',
            name='source',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datadata',
            name='start_year',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datadata',
            name='topic',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datadata',
            name='url',
            field=models.TextField(blank=True, null=True),
        ),
    ]