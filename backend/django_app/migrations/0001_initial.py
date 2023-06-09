# Generated by Django 4.1.7 on 2023-03-27 15:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, default='default/account/default_avatar.jpg', help_text='<small class="text-muted"ImageField [jpg, png]</small><hr><br>', max_length=200, null=True, upload_to='uploads/admin/account/avatar', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png'])], verbose_name='Изображение')),
                ('user', models.ForeignKey(blank=True, default=None, help_text='<small class="text-muted">ForeignKey</small><hr><br>', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пользователь расширение',
                'verbose_name_plural': 'Admin 1, Пользователи расширение',
                'ordering': ('-id',),
            },
        ),
    ]
