# Generated by Django 5.0.3 on 2024-03-05 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0002_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelreg',
            name='password',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='img',
            name='Image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
