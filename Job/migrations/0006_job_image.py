# Generated by Django 4.0.6 on 2022-07-28 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0005_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', upload_to='jobs/'),
            preserve_default=False,
        ),
    ]
