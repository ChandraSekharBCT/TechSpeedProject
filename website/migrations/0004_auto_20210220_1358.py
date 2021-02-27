# Generated by Django 2.2.5 on 2021-02-20 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_work_withus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work_withuss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expert_name', models.CharField(max_length=255)),
                ('expert_email', models.EmailField(max_length=254)),
                ('expert_phone_number', models.CharField(max_length=12)),
                ('resume_url', models.FileField(upload_to='resume/')),
                ('background', models.FileField(upload_to='background/')),
                ('subject', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Work_withus',
        ),
    ]
