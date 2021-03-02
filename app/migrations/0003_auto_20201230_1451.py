# Generated by Django 3.0.7 on 2020-12-30 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_lessons_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='classes',
            name='student_quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='section',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='week',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='subject',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
