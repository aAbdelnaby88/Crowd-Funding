# Generated by Django 2.1.5 on 2020-03-31 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_confirmation', models.BooleanField(default=False, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='Phone')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='FaceBook')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='BirthDate')),
                ('user_image', models.ImageField(default='images/users/default.jpg', upload_to='images/users/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User Name')),
            ],
        ),
    ]
