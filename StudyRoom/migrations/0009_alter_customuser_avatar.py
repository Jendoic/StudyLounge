# Generated by Django 4.0.4 on 2024-07-11 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyRoom', '0008_alter_customuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]