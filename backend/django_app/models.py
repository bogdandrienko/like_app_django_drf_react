from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    """
    Модель, которая содержит расширение для стандартной модели пользователя веб-платформы
    """
    user = models.OneToOneField(
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Пользователь',
        help_text='<small class="text-muted">ForeignKey</small><hr><br>',
        to=User,
        on_delete=models.SET_NULL,
        related_name='profile',
    )
    avatar = models.ImageField(
        validators=[FileExtensionValidator(['jpg', 'png'])],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='default/account/default_avatar.jpg',
        verbose_name='Изображение',
        help_text='<small class="text-muted"ImageField [jpg, png]</small><hr><br>',

        upload_to='uploads/admin/account/avatar',
        max_length=200,
    )
    # mobile, bio

    class Meta:
        app_label = 'django_app'
        ordering = ('-id',)
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.user} {self.id}'


@receiver(post_save, sender=User)
def create_user_model(sender, instance, created, **kwargs):
    if created:  # todo в первый ли раз
        try:
            Profile.objects.get_or_create(user=instance)
        except Exception as error:
            pass
